#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AST doesn't conform to snake_case naming style + return:
# pylint: disable=invalid-name, too-many-return-statements, too-many-branches
"""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
from __future__ import annotations

import ast
import re
from collections import deque
from functools import wraps
from typing import TypeVar, NamedTuple, Optional, Union, Callable, Any, cast

from docstring2md.__config__ import LOGGING_MSG, TAG
from docstring2md.convmd import ConvMD
from docstring2md.log import logger

F = TypeVar('F', bound=Callable[..., Any])
ASTNode = Union[ast.Module, ast.ClassDef, ast.FunctionDef]
ASTClassFunc = Union[ast.ClassDef, ast.FunctionDef]


def logger_ast(func: F) -> F:
    """
    This function is a decorator to use in the AST Navigator Class.

    Args:
                func: F (Callable[..., Any])

    Returns:
                F (Callable[..., Any])

    """

    @wraps(func)
    def func_wrapper(*args: Any, **kwargs: Any) -> Any:
        target: str = ""
        msg_debug: Optional[str] = None
        for arg in args:
            if isinstance(arg, (ast.FunctionDef, ast.ClassDef)):
                target = arg.name
                msg_debug = ast.dump(arg)
        if str(func.__name__).startswith("visit_"):
            logger.info("%s(): %s", func.__name__, target)
            if msg_debug:
                logger.debug(msg_debug)
        else:
            msg = f"{func.__name__}(): {target}" if target != "" \
                else f"{func.__name__}()"
            logger.debug(msg)
        return func(*args, **kwargs)

    return cast(F, func_wrapper)


class NodeLink(NamedTuple):
    """
    NamedTuple to link a node with a parent Node

    Attributes:
        level (int): level in the module
        parent (NodeType): parent

    """
    level: int
    parent: Optional[ASTNode]


class ModuleDef(NamedTuple):
    """
    NamedTuple to define a Module.

    Examples:
        >>> mydocstring = "Title:"
        >>> module = ModuleDef(docstring=mydocstring)
        >>> module
        ModuleDef(docstring='Title:')
        >>> module.get_summary()
        '# Title:'
    """
    docstring: str

    def get_summary(self) -> str:
        """
        get the module's summary

        Returns:
            str: Summary
        """
        return self.get_docstring()

    @ConvMD.dedent()
    @ConvMD.repl_beg_end(TAG.beg_str, TAG.end_strh,
                         TAG.tab + TAG.beg_title + TAG.space, TAG.end_title)
    def get_docstring(self) -> str:
        """
        Generate the module's Docstring with MD Tag.

        Returns:
            str: Docstring

        """
        return self.docstring


class NodeDef(NamedTuple):
    """
    NamedTuple to define a node (Class/Function)

    Attributes:
        title (str): short class/function definition
        definition (str): full class/function definition
        docstring (str): docstring
        level (int): level in the module

    """
    title: str
    definition: str
    docstring: str
    level: int

    def get_summary(self) -> str:
        """
        Node's summary

        Returns:
            str

        """
        return f"{self.get_title()}{TAG.cr}{self.get_definition()}{TAG.cr}" + \
            f"{self.get_docstring()}"

    def get_toc_elem(self) -> str:
        """
        Return a TOC entry for this node

        Returns:
            str

        """
        anchor: str = f"{self.title}"
        anchor = re.sub(r"__([a-zA-Z_]*)__\(", r"\1(", anchor)
        anchor = re.sub(
            r"[^\w\- ]+", "", (anchor.replace(' ', '-')).lower())
        return f"[{self.title}](#{anchor})<br />"

    def get_title(self) -> str:
        """
        Return the node's title

        Returns:
            str

        """
        return f"{'#' * (self.level + 2)} {self.title}"

    @ConvMD.add_tag(TAG.beg_py, TAG.end_py)
    def get_definition(self) -> str:
        """
        Return a TOC entry for this node

        Returns:
            str

        """
        return self.definition

    @ConvMD.repl_beg_end(TAG.beg_str, TAG.end_strh, TAG.beg_b, TAG.end_bh)
    @ConvMD.colorize_examples()
    @ConvMD.add_tag(TAG.cr, TAG.cr)
    def get_docstring(self) -> str:
        """
        Generate the node's Docstring with MD Tag.

        Returns:
            str: Docstring

        """
        return self.docstring


NodeListType = deque[Union[NodeDef, ModuleDef]]


class ObjVisitor(ast.NodeVisitor):
    """
    This Class is an ast.NodeVisitor class and allow us to parse
    code tree.
    All methods are called according to node type.
    We define other private method in order to manage string format.
    We use decorator to keep a clean code without MD Tag.

    ObjVisitor(module_docstring=True|False)
        module_docstring: true => retrieve the module docstring
        This parameter is usefull to use the first docstring module
        in a package.

    Examples:
        >>> from docstring2md.file import MyFile
        >>> import pathlib
        >>> module = str(pathlib.Path(__file__).resolve())
        >>> source = MyFile.set_path(module)
        >>> # init
        >>> doc = ObjVisitor(module_docstring=False)
        >>> # provide source, generate the tree and use visit mechanism
        >>> doc.visit(doc.parse(source.read()))
        >>> result = doc.node_lst
        >>> result[0].title
        'logger_ast()'
        >>> result[0].get_toc_elem()
        '[logger_ast()](#logger_ast)<br />'
        >>> result[0].definition
        'def logger_ast(func: F) -> F:'

    """
    __module_docstring: bool
    __private_def: bool
    __func: list[Any]

    def __init__(
            self, module_docstring: bool = False, private_def: bool = False) \
            -> None:
        super(ast.NodeVisitor, self).__init__()
        self.__module_docstring = module_docstring
        self.__private_def = private_def
        self.__link_lst: dict[ASTNode, NodeLink]
        self.__node_lst: NodeListType = deque()

    @property
    def node_lst(self) -> NodeListType:
        """Return node list"""
        return self.__node_lst

    @staticmethod
    def parse(source: str) -> ast.AST:
        """
        Parse the source code and build the tree.

        Args:
            source (str): source code

        Returns:
            AST tree

        """
        return ast.parse(source)

    @logger_ast
    def __set_level(
            self, node: ASTNode, level: int = 0,
            parent: Optional[ASTNode] = None)\
            -> None:
        if level == 0:
            logger.info(LOGGING_MSG.node_link_analysis_beg.info)
            self.__link_lst = {}
        self.__link_lst[node] = NodeLink(level=level, parent=parent)

        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef)):
                self.__set_level(child, (level + 1), node)
        if level == 0:
            logger.info(LOGGING_MSG.node_link_analysis_end.info)

    # -------------------------------------------------------------------------
    # Generic
    # -------------------------------------------------------------------------

    @logger_ast
    def __get_fullname(self, node: ASTClassFunc) -> str:
        node_link: NodeLink = self.__link_lst[node]
        return node.name if isinstance(node_link.parent, ast.Module) \
            else f"{self.__get_fullname(node_link.parent)}.{node.name}" if \
            node_link.parent is not None else ""

    @staticmethod
    @logger_ast
    def __get_docstring(node: ASTNode) -> str:
        return str(ast.get_docstring(node))

    @staticmethod
    def __get_value_from_name(node: ast.Name) -> str:
        return node.id

    @staticmethod
    def __get_value_from_constant(
            node: Union[ast.Constant, ast.NameConstant]) -> str:
        return node.value

    @staticmethod
    def __get_value_from_num(node: ast.Num) -> str:
        return str(node.n)

    @staticmethod
    def __get_value_from_str(node: ast.Str) -> str:
        return node.s

    @staticmethod
    def __get_value_from_attribute(node: ast.Attribute) -> str:
        return f"{node.value.id}.{node.attr}" \
            if isinstance(node.value, ast.Name) else ""

    @staticmethod
    def __get_value_from_unary(node: ast.UnaryOp) -> str:
        return f"-{node.operand.id}" \
            if isinstance(node.operand, ast.Name) else ""

    def __get_value_from_list(self, node: ast.List) -> str:
        elts_lst: list[str] = [
            self.__get_value_from_node(elt) for elt in node.elts
            if isinstance(elt, (ast.Num, ast.Constant, ast.Subscript, ast.Str,
                                ast.Name, ast.NameConstant, ast.Attribute))]
        elts = ", ".join(elts_lst)
        return f"[{elts}]"

    def __get_value_from_subscript(self, node: ast.Subscript) -> str:
        if isinstance(node.value, ast.Name):
            curr_value = node.value
            curr_slice = node.slice
            _elts = ""
            # multiple elts
            if hasattr(curr_slice, "elts"):
                for elt in curr_slice.elts:
                    if isinstance(elt, ast.List):
                        _elts = f"{_elts}{self.__get_value_from_node(elt)}, "
                    elif isinstance(elt, (ast.Attribute, ast.Subscript,
                                          ast.Name, ast.Constant)):
                        _elts = f"{_elts}{self.__get_value_from_node(elt)}, "
                _elts = _elts[:-2] if _elts.endswith(", ") else _elts
                return f"{curr_value.id}[{_elts}]"
            if isinstance(curr_slice, ast.Subscript):
                _elts = f"[{self.__get_value_from_node(curr_slice)}]"
            if isinstance(curr_slice, (ast.Name, ast.Attribute)):
                _elts = f"{self.__get_value_from_node(curr_slice)}"
            if isinstance(curr_slice, ast.Name):
                _elts = f"[{_elts}]"
            return f"{curr_value.id}{_elts}"
        return ""

    @logger_ast
    def __get_value_from_node(
            self, node: Union[
                ast.Name, ast.Constant, ast.NameConstant, ast.Num, ast.Str,
                ast.Attribute, ast.Subscript, ast.UnaryOp, ast.List]) -> str:

        methode_by_type: dict[Any, Callable[..., str]] = {
            ast.Name: self.__get_value_from_name,
            ast.Constant: self.__get_value_from_constant,
            ast.NameConstant: self.__get_value_from_constant,
            ast.Num: self.__get_value_from_num,
            ast.Str: self.__get_value_from_str,
            ast.Attribute: self.__get_value_from_attribute,
            ast.List: self.__get_value_from_list,
            ast.Subscript: self.__get_value_from_subscript,
            ast.UnaryOp: self.__get_value_from_unary}

        result: str = methode_by_type[type(node)](node) \
            if type(node) in methode_by_type else ""

        if result == "":
            logger.warning(
                LOGGING_MSG.unknown_type_of_node.warning, str(ast.dump(node)))

        return result

    # -------------------------------------------------------------------------
    # Module
    # -------------------------------------------------------------------------
    @logger_ast
    def visit_Module(self, node: ast.Module) -> None:
        """
        This function is automatically called by AST mechanism
        when the current node is a module.
        We update self.node_lst.

        Args:
            node (ast.AST): current node

        Returns:
            None
        """
        # Find all objects and set up the level
        self.__set_level(node)
        # Get docstring if available
        if self.__module_docstring:
            self.__node_lst.append(ModuleDef(
                docstring=self.__mod_get_docstring(node)))
        # Continue the visit
        self.generic_visit(node)

    def __mod_get_docstring(self, node: ast.Module) -> str:
        return self.__get_docstring(node)

    # -------------------------------------------------------------------------
    # Class
    # -------------------------------------------------------------------------
    @logger_ast
    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """
        This function is automatically called by AST mechanism
        when the current node is a class.
        We update self.node_lst.

        Args:
            node (ast.ClassDef): current node

        Returns:
            None
        """
        self.__node_lst.append(
            NodeDef(
                title=self.__cla_get_title(node),
                definition=self.__cla_get_def(node),
                docstring=self.__cla_get_docstring(node),
                level=self.__link_lst[node].level))
        self.generic_visit(node)

    @logger_ast
    def __cla_get_title(self, node: ast.ClassDef) -> str:
        return f"{node.name}()"

    @logger_ast
    def __cla_get_def(self, node: ast.ClassDef) -> str:
        return f"class {node.name}({self.__cla_get_inheritance(node)}):"

    @logger_ast
    def __cla_get_inheritance(self, node: ast.ClassDef) -> str:
        return TAG.coma.join([self.__get_value_from_node(base)
                              for base in node.bases
                              if isinstance(base, (ast.Name, ast.Attribute))])

    @logger_ast
    def __cla_get_docstring(self, node: ast.ClassDef) -> str:
        return self.__get_docstring(node)

    # -------------------------------------------------------------------------
    # Function
    # -------------------------------------------------------------------------
    @logger_ast
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        This function is automatically called by AST mechanism
        when the current node is a function.
        We add FuncDef obj in self.node_lst.

        Args:
            node (ast.FunctionDef): current node

        Returns:
            None

        """
        if self.__func_valid_name(node):
            self.__node_lst.append(NodeDef(
                title=self.__func_get_title(node),
                definition=self.__func_get_def(node),
                docstring=self.__func_get_docstring(node),
                level=self.__link_lst[node].level))
        self.generic_visit(node)

    @logger_ast
    def __func_valid_name(self, node: ast.FunctionDef) -> bool:
        return self.__private_def or (node.name.startswith("__") is False)

    @logger_ast
    def __func_get_title(self, node: ast.FunctionDef) -> str:
        title = f"{self.__get_fullname(node)}()"
        return f"@Property {title}" \
            if "@property" in self.__func_get_decorator(node) \
            else f"{title}"

    @logger_ast
    def __func_get_def(self, node: ast.FunctionDef) -> str:
        deco: str = TAG.cr.join(self.__func_get_decorator(node)) + TAG.cr \
            if (hasattr(node, "decorator_list")
                and len(node.decorator_list) > 0) else ""
        return f"{deco}def {self.__get_fullname(node)}" + \
            f"({self.__func_get_args(node)}){self.__func_get_return(node)}:"

    @logger_ast
    def __func_get_args(self, node: ast.FunctionDef) -> str:
        argument: list[str] = [arg.arg + self.__func_get_args_annotation(arg)
                               for arg in node.args.args]
        if len(node.args.defaults) > 0:
            def_value: list[str] = [""] * (len(argument) - len(
                node.args.defaults)) + self.__func_get_args_default(node)
            argument = [arg + def_value[idx] for idx, arg in
                        enumerate(argument)]
        if hasattr(node.args, "vararg") and node.args.vararg:
            argument.append(
                f"*{node.args.vararg.arg}" +
                f"{self.__func_get_args_annotation(node.args.vararg)}")
        if hasattr(node.args, "kwarg") and node.args.kwarg:
            argument.append(
                f"**{node.args.kwarg.arg}" +
                f"{self.__func_get_args_annotation(node.args.kwarg)}")

        result: str = f"{TAG.coma.join(argument)}"
        return result

    @logger_ast
    def __func_get_args_annotation(self, node: ast.arg) -> str:
        return f": {self.__get_value_from_node(node.annotation)}" \
            if (hasattr(node, "annotation")
                and isinstance(node.annotation, (ast.Name,
                                                 ast.Attribute,
                                                 ast.Subscript))) \
            else ""

    @logger_ast
    def __func_get_args_default(self, node: ast.FunctionDef) -> list[str]:
        return [f" = {self.__get_value_from_node(def_value)}"
                for def_value in node.args.defaults
                if isinstance(def_value, (ast.Constant,
                                          ast.NameConstant,
                                          ast.Num,
                                          ast.Str,
                                          ast.Name,
                                          ast.Attribute,
                                          ast.UnaryOp))]

    @logger_ast
    def __func_get_decorator(self, node: ast.FunctionDef) -> list[str]:
        decorator: list[str] = []
        name: str
        for dec in node.decorator_list:
            name = ''
            if isinstance(dec, (ast.Name, ast.Attribute)):
                name = self.__get_value_from_node(dec)
            elif isinstance(dec, ast.Call):
                if isinstance(dec.func, (ast.Attribute, ast.Name)):
                    name = self.__get_value_from_node(dec.func)
                if hasattr(dec, "args"):
                    name += self.__func_get_decorator_args(dec)
            decorator.append("@" + name)
        return decorator

    @logger_ast
    def __func_get_decorator_args(self, node: ast.Call) -> str:
        # node = Args from Call node
        return TAG.coma.join([self.__get_value_from_node(attribute)
                              for attribute in node.args
                              if isinstance(attribute, (ast.Name,
                                                        ast.Attribute))])

    @logger_ast
    def __func_get_return(self, node: ast.FunctionDef) -> str:
        return f" -> {self.__get_value_from_node(node.returns)}" \
            if (node.returns is not None
                and isinstance(node.returns, (ast.Name,
                                              ast.Constant,
                                              ast.Attribute,
                                              ast.Subscript))) \
            else ""

    @logger_ast
    def __func_get_docstring(self, node: ast.FunctionDef) -> str:
        return self.__get_docstring(node)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
