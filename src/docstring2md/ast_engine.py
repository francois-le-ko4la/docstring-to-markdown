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
from typing import NamedTuple, Union, Callable, Any
from collections import deque

from docstring2md.__config__ import TAG
from docstring2md.convmd import ConvMD
from docstring2md.log import logger


def logger_ast(cur_func: Callable[..., Any]) -> Any:
    """
    This function is a decorator to use in the AST Navigator Class.

    Args:
        cur_func: Callable[P, Any]

    Returns:
        Callable[P, Any]

    """
    def inner(*args: object, **kwargs: object) -> Any:
        msg = f"{cur_func.__name__}"
        msg_debug: Union[None, str] = None

        for arg in args:
            if isinstance(arg, (ast.FunctionDef, ast.ClassDef)):
                msg = f"{msg}: {arg.name}"
                msg_debug = ast.dump(arg)
        if str(cur_func.__name__).startswith("visit_"):
            logger.info(msg)
            if msg_debug:
                logger.debug(msg_debug)
        else:
            logger.debug(msg)
        return cur_func(*args, **kwargs)
    return inner


class NodeLink(NamedTuple):
    """NamedTuple to link a node with a parent Node"""
    level: int
    parent: Union[ast.FunctionDef, ast.ClassDef, ast.Module]


class NodeDef(NamedTuple):
    """NamedTuple to link a node with a parent Node"""
    title: str
    definition: str
    docstring: str
    level: int

    def get_summary(self) -> str:
        """Node summary

        Returns:
            str

        """
        return f"{self.get_title()}\n{self.get_definition()}\n" + \
               f"{self.get_docstring()}"

    def get_toc_elem(self) -> str:
        """Return a TOC entry for this node

        Returns:
            str

        """
        anchor: str = f"{self.title}"
        anchor = re.sub(r"__([a-zA-Z_]*)__\(", r"\1(", anchor)
        anchor = re.sub(
            r"[^\w\- ]+", "", (anchor.replace(' ', '-')).lower())
        return f"[{self.title}](#{anchor})<br />"

    def get_title(self) -> str:
        """Return the node's title

        Returns:
            str

        """
        return f"{'#' * (self.level + 3)} {self.title}"

    @ConvMD.add_tag(TAG.beg_py, TAG.end_py)
    def get_definition(self) -> str:
        """Return a TOC entry for this node

        Returns:
            str

        """
        return self.definition

    @ConvMD.add_tag(TAG.beg_co, TAG.end_co)
    def get_docstring(self) -> str:
        """Return the node's docstring.

        Returns:
            str

        """

        return self.docstring


class ClassDef(NodeDef):
    """Define a Class node.

    Returns:
        ClassDef

    """
    def __new__(cls, *arg, **kwargs) -> ClassDef:
        return super().__new__(ClassDef, *arg, **kwargs)

    def __init__(
            self, title: str, definition: str, docstring: str, level: int):
        logger.debug(
            "New ClassDef - title: %s / def: %s / doc: %s / lvl: %s",
            title, definition, docstring, level)


class FuncDef(NodeDef):
    """Define a Function node.

    Returns:
        FuncDef

    """
    def __new__(cls, *args, **kwargs) -> FuncDef:
        return super().__new__(FuncDef, *args, **kwargs)

    def __init__(
            self, title: str, definition: str, docstring: str, level: int):
        logger.debug(
            "New FuncDef - title: %s / def: %s / doc: %s / lvl: %s",
            title, definition, docstring, level)

    @ConvMD.repl_beg_end(TAG.beg_str, TAG.end_str, TAG.quote, TAG.html_cr)
    @ConvMD.repl_beg_end(TAG.beg_str, TAG.end_strh, TAG.beg_b, TAG.end_bh)
    @ConvMD.repl_str(TAG.tab, TAG.html_tab)
    @ConvMD.add_tag(TAG.cr, TAG.cr)
    def get_docstring(self) -> str:
        return self.docstring


class ModuleDef(NodeDef):
    """Define a Module node.

    Returns:
        ModuleDef

    """
    def __new__(cls, *args, **kwargs) -> ModuleDef:
        return super().__new__(ModuleDef, *args, **kwargs)

    def __init__(
            self, title: str, definition: str, docstring: str, level: int):
        logger.debug(
            "New ModuleDef - title: %s / def: %s / doc: %s / lvl: %s",
            title, definition, docstring, level)


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

    Use:
        >>> from docstring2md.file import MyFile
        >>> import pathlib
        >>> module = str(pathlib.Path(__file__).resolve())
        >>> source = MyFile.set_path(module)
        >>> # init
        >>> doc = ObjVisitor(module_docstring=False)
        >>> # provide source, generate the tree and use visit mechanism
        >>> doc.visit(doc.get_tree(source.read()))
        >>> result = doc.node_lst
        >>> result[0].title
        'logger_ast()'
        >>> result[0].get_toc_elem()
        '[logger_ast()](#logger_ast)<br />'
    """
    __module_docstring: bool
    __priv: bool
    __func: list[Any]

    def __init__(
            self, module_docstring: bool = False, priv: bool = False) -> None:
        super(ast.NodeVisitor, self).__init__()
        self.__module_docstring = module_docstring
        self.__priv = priv
        self.__link_lst: dict[
            Union[ast.FunctionDef, ast.ClassDef, ast.Module], NodeLink]
        self.__node_lst: deque[
            Union[ModuleDef, ClassDef, FuncDef, None]] = deque()

    @property
    def node_lst(self) -> deque[Union[ModuleDef, ClassDef, FuncDef, None]]:
        """Return node list"""
        return self.__node_lst

    @staticmethod
    def get_tree(source: str) -> ast.AST:
        """
        This function allow us to parse the source and build the
        tree.
        We put this function to group all AST function in this
        module.

        Args:
            source (str): source code

        Returns:
            AST tree

        """
        return ast.parse(source)

    @logger_ast
    def __set_level(
            self, node: Union[ast.Module, ast.ClassDef, ast.FunctionDef],
            level=0, parent=None) -> None:
        if level == 0:
            logger.info("start node link analysys: begin")
            self.__link_lst = {}
        self.__link_lst[node] = NodeLink(level=level, parent=parent)

        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef)):
                self.__set_level(child, (level+1), node)
        if level == 0:
            logger.info("start node link analysys: end")

    # -------------------------------------------------------------------------
    # Generic
    # -------------------------------------------------------------------------

    @logger_ast
    def __get_fullname(self,
                       node: Union[
                           ast.FunctionDef, ast.ClassDef]) -> str:
        node_link: NodeLink = self.__link_lst[node]
        if isinstance(node_link.parent, ast.Module):
            return node.name
        return f"{self.__get_fullname(node_link.parent)}.{node.name}"

    @staticmethod
    @logger_ast
    def __get_docstring(
        node: Union[
            ast.Module, ast.ClassDef, ast.FunctionDef]) -> str:
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
        if isinstance(node.value, ast.Name):
            return f"{node.value.id}.{node.attr}"
        logger.warning("__get_value_from_attribute - another object: %s",
                       str(ast.dump(node)))
        return ""

    @staticmethod
    def __get_value_from_unary(node: ast.UnaryOp) -> str:
        if isinstance(node.operand, ast.Name):
            return f"-{node.operand.id}"
        logger.warning("__get_value_from_unary - another object: %s",
                       str(ast.dump(node)))
        return ""

    def __get_value_from_subscript(self, node: ast.Subscript) -> str:
        if isinstance(node.value, ast.Name):
            curr_value = node.value
            curr_slice = node.slice
            _elts = ""
            # multiple elts
            if hasattr(curr_slice, "elts"):
                for elt in curr_slice.elts:
                    if isinstance(elt, ast.List):
                        sub_str = [
                            self.__get_value_from_node(sub) for sub in
                            elt.elts if
                            isinstance(sub, (ast.Name, ast.Constant,
                                             ast.NameConstant, ast.Num,
                                             ast.Subscript, ast.Attribute,
                                             ast.Str))]
                        _elts = ", ".join(sub_str)
                        _elts = f"[{_elts}], "
                    elif isinstance(elt, (
                            ast.Name, ast.Constant, ast.Attribute,
                            ast.Subscript)):
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
        logger.warning("__get_value_from_subscript - another object: %s",
                       str(ast.dump(node)))
        return ""

    @logger_ast
    def __get_value_from_node(
            self, node: Union[
                ast.Name, ast.Constant, ast.NameConstant, ast.Num, ast.Str,
                ast.Attribute, ast.Subscript, ast.UnaryOp]) -> str:

        methode_by_type: dict[Any, Callable[..., str]] = {
            ast.Name: self.__get_value_from_name,
            ast.Constant: self.__get_value_from_constant,
            ast.NameConstant: self.__get_value_from_constant,
            ast.Num: self.__get_value_from_num,
            ast.Str: self.__get_value_from_str,
            ast.Attribute: self.__get_value_from_attribute,
            ast.Subscript: self.__get_value_from_subscript,
            ast.UnaryOp: self.__get_value_from_unary}

        if type(node) in methode_by_type:
            func: Callable[..., str] = methode_by_type[type(node)]
            return func(node)
        logger.warning("__get_value_from_node - another object: %s",
                       str(ast.dump(node)))
        return ""

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
            None.
        """
        # Find all objects and set up the level
        self.__set_level(node)
        # Get docstring if available
        if self.__module_docstring:
            self.__node_lst.append(
                ModuleDef(
                    title="Module", definition="",
                    docstring=self.__mod_get_docstring(node), level=0))
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
            node (ast): current node

        Returns:
            None.
        """
        self.__node_lst.append(
            ClassDef(
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
        return f"class {node.name}{self.__cla_get_inheritance(node)}:"

    @logger_ast
    def __cla_get_inheritance(self, node: ast.ClassDef) -> str:
        bases: list = [self.__get_value_from_node(base)
                       for base in node.bases
                       if isinstance(base, (ast.Name, ast.Attribute))]
        return f"({', '.join(bases)})"

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
        We update self.node_lst.

        Args:
            node (ast.AST): current node

        Returns:
            None.
        """
        if self.__func_valid_name(node):
            self.__node_lst.append(FuncDef(
                title=self.__func_get_title(node),
                definition=self.__func_get_def(node),
                docstring=self.__func_get_docstring(node),
                level=self.__link_lst[node].level))
        self.generic_visit(node)

    @logger_ast
    def __func_valid_name(self, node: ast.FunctionDef) -> bool:
        return self.__priv or (node.name.startswith("__") is False)

    @logger_ast
    def __func_get_title(self, node: ast.FunctionDef) -> str:
        fullname = self.__get_fullname(node)
        return f"@Property {fullname}()" \
            if "@property" in self.__func_get_decorator(node) \
            else f"{fullname}()"

    @logger_ast
    def __func_get_def(self, node: ast.FunctionDef) -> str:
        decorator: str = ""
        if hasattr(node, "decorator_list"):
            decorator_lst: list[str] = self.__func_get_decorator(node)
            decorator = "{}\n".format(
                '\n'.join(decorator_lst)) if len(decorator_lst) > 0 else ""
        return f"{decorator}def {self.__get_fullname(node)}" + \
            f"{self.__func_get_args(node)}{self.__func_get_return(node)}:"

    @logger_ast
    def __func_get_args(self, node: ast.FunctionDef) -> str:
        argument: list[str] = [arg.arg + self.__func_get_args_annotation(arg)
                               for index, arg in enumerate(node.args.args)]
        if len(node.args.defaults) > 0:
            def_value = [""] * (len(argument) - len(node.args.defaults)) + \
                        self.__func_get_args_default(node)
            argument = [arg+def_value[idx] for idx, arg in enumerate(argument)]
        if hasattr(node.args, "vararg") and node.args.vararg:
            argument.append(
                f"*{node.args.vararg.arg}" +
                f"{self.__func_get_args_annotation(node.args.vararg)}")
        if hasattr(node.args, "kwarg") and node.args.kwarg:
            argument.append(
                f"**{node.args.kwarg.arg}" +
                f"{self.__func_get_args_annotation(node.args.kwarg)}")

        return f"({', '.join(argument)})"

    @logger_ast
    def __func_get_args_annotation(self, node: ast.arg) -> str:
        if (hasattr(node, "annotation")
                and isinstance(node.annotation, (ast.Name,
                                                 ast.Attribute,
                                                 ast.Subscript))):
            return f": {self.__get_value_from_node(node.annotation)}"
        return ""

    @logger_ast
    def __func_get_args_default(self, node: ast.FunctionDef) -> list[str]:
        result: list[str] = []

        for def_value in node.args.defaults:
            if isinstance(def_value, (ast.Constant,
                                      ast.NameConstant,
                                      ast.Num,
                                      ast.Str,
                                      ast.Name,
                                      ast.Attribute,
                                      ast.UnaryOp)):
                result.append(f" = {self.__get_value_from_node(def_value)}")
            else:
                logger.warning("another kind of default value: %s", def_value)

        return result

    @logger_ast
    def __func_get_decorator(self, node: ast.FunctionDef) -> list:
        decorator = []
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
        args: list[str] = []
        for attribute in node.args:
            if isinstance(attribute, (ast.Name, ast.Attribute)):
                args.append(self.__get_value_from_node(attribute))
        return f"({', '.join(args)})"

    @logger_ast
    def __func_get_return(self, node: ast.FunctionDef) -> str:
        if node.returns is None:
            return ""
        if isinstance(node.returns, (ast.Name,
                                     ast.Constant,
                                     ast.Attribute,
                                     ast.Subscript)):
            return f" -> {self.__get_value_from_node(node.returns)}"
        logger.warning("another kind of returns: %s", node.returns)
        logger.warning(ast.dump(node))
        return ""

    @logger_ast
    def __func_get_docstring(self, node: ast.FunctionDef) -> str:
        return self.__get_docstring(node)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
