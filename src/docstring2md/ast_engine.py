#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AST doesn't conform to snake_case naming style:
# pylint: disable=invalid-name, too-many-branches
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
from typing import NamedTuple, Any, Union, Optional

from docstring2md.__config__ import TAG, BLACKLIST
from docstring2md.convmd import ConvMD
from docstring2md.log import logger


class NodeLink(NamedTuple):
    """NamedTuple to link a node with a parent Node"""
    level: int
    parent: Union[ast.FunctionDef, ast.ClassDef, ast.Module]


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
        >>> # provide source, generate the tree and use visit mechanisme
        >>> doc.visit(doc.get_tree(source.read()))
        >>> result = doc.output
        >>> result = result.split("\\n")
        >>> result[0]
        '#### NodeLink()'
    """
    __toc: list[Any]
    __output: list[Any]
    __module_docstring: bool
    __priv: bool
    __func: list[Any]

    def __init__(self, module_docstring: bool = False, priv: bool = False) ->\
            None:
        super(ast.NodeVisitor, self).__init__()
        self.__toc = []
        self.__output = []
        self.__module_docstring = module_docstring
        self.__priv = priv
        self.__func = []
        self.__link_lst: dict[
            Union[ast.FunctionDef, ast.ClassDef, ast.Module], NodeLink]

    @property
    def toc(self) -> str:
        """Return toc property"""
        return "\n".join(self.__toc)

    @property
    def output(self) -> str:
        """Return output property"""
        return "\n".join(self.__output)

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

    def __set_level(self, node, level=0, parent=None) -> None:
        if level == 0:
            self.__link_lst = {}
        self.__link_lst[node] = NodeLink(level=level, parent=parent)

        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef)):
                self.__set_level(child, (level+1), node)

    def visit_Module(self, node: ast.Module) -> None:
        """
        This function is automatically called by AST mechanisme
        when the current node is a module.
        We update self.output.

        Args:
            node (ast.AST): current node

        Returns:
            None.
        """
        logger.info("visit module: %s", node)
        self.__set_level(node)
        if self.__module_docstring:
            self.__output.append(self.__get_docstring(node))
        self.generic_visit(node)

    def __add_toc(self, title: str) -> None:
        anchor: str = title
        anchor = re.sub(r"__([a-zA-Z_]*)__\(", r"\1(", anchor)
        anchor = re.sub(
            r"[^\w\- ]+", "", (anchor.replace(' ', '-')).lower())
        self.__toc.append(f"[{title}](#{anchor})<br />")

    @staticmethod
    def __get_args(node: ast.FunctionDef) -> str:
        argument: list[str] = []
        value: Union[str, int, complex]

        logger.debug("get args from: %s", node.name)

        for arg in node.args.args:
            str_annot = ""
            if isinstance(arg.annotation, ast.Name):
                curr_name = arg.annotation
                str_annot = f": {curr_name.id}"
            elif isinstance(arg.annotation, ast.Attribute):
                curr_value: Union[ast.Name, ast.expr] = arg.annotation.value
                if isinstance(curr_value, ast.Name):
                    str_annot = f": {curr_value.id}.{arg.annotation.attr}"
            elif isinstance(arg.annotation, ast.Subscript):
                curr_value = arg.annotation.value
                curr_slice = arg.annotation.slice
                if (hasattr(curr_slice, "elts")
                        and isinstance(curr_value, ast.Name)):
                    _elts = ""
                    for elts in curr_slice.elts:
                        if isinstance(elts, ast.Constant):
                            _elts = f"{_elts}{elts.value}, "
                        if isinstance(elts, ast.Name):
                            _elts = f"{_elts}{elts.id}, "
                        if (isinstance(elts, ast.Attribute) and
                                isinstance(elts.value, ast.Name)):
                            _elts = f"{_elts}{elts.value.id}.{elts.attr}, "
                    str_annot = f": {curr_value.id}[{_elts[:-2]}]"
                else:
                    if (isinstance(curr_slice, ast.Attribute)
                            and isinstance(curr_slice.value, ast.Name)
                            and isinstance(curr_value, ast.Name)):
                        str_annot = f": {curr_value.id}[" \
                                    f"{curr_slice.value.id}.{curr_slice.attr}]"
            argument.append(arg.arg + str_annot)

        idx = len(argument) - len(node.args.defaults)
        for expr in node.args.defaults:
            value = "unknown"
            if isinstance(expr, ast.Num):
                value = expr.n
            elif isinstance(expr, ast.Str):
                value = expr.s
            elif isinstance(expr, ast.NameConstant):
                value = expr.value
            argument[idx] = argument[idx] + "=" + str(value)
            idx += 1

        if hasattr(node.args, "vararg") and node.args.vararg:
            argument.append(f"*{node.args.vararg.arg}")

        if hasattr(node.args, "kwarg") and node.args.kwarg:
            argument.append(f"**{node.args.kwarg.arg}")

        return f"({', '.join(argument)})"

    @staticmethod
    def __get_decorator_args(node: list[ast.expr]) -> str:
        # node = Args from Call node
        args: list[str] = []
        logger.debug("__get_decorator_args")
        for attribute in node:
            if isinstance(attribute, ast.Name):
                args.append(attribute.id)
            if (isinstance(attribute, ast.Attribute) and
                    isinstance(attribute.value, ast.Name)):
                curr_value = attribute.value
                attribute_id = curr_value.id
                attribute_attr = "." + attribute.attr if hasattr(
                    attribute, "attr") else ""
                args.append(attribute_id + attribute_attr)

        return f"({', '.join(args)})"

    def __get_decorator(self, node: ast.FunctionDef) -> list:
        decorator = []
        name: str

        logger.debug("get decorator from: %s", node.name)

        for dec in node.decorator_list:
            name = ''
            if isinstance(dec, ast.Name):
                name = dec.id
            elif isinstance(dec, ast.Attribute):
                name = dec.attr
            elif isinstance(dec, ast.Call):
                if (isinstance(dec.func, ast.Attribute) and isinstance(
                        dec.func.value, ast.Name)):
                    curr_value: ast.Name = dec.func.value
                    name = curr_value.id
                elif isinstance(dec.func, ast.Name):
                    name = dec.func.id
                if hasattr(dec.func, "attr"):
                    name = ".".join([name, dec.func.attr])
                if hasattr(dec, "args"):
                    name += self.__get_decorator_args(dec.args)  # ?????
                    # name += self.__get_args(dec.func)
            decorator.append("@" + name)

        return decorator

    def __get_fullname(self,
                       node: Union[
                           ast.FunctionDef, ast.ClassDef]) -> str:

        node_link: NodeLink = self.__link_lst[node]
        if isinstance(node_link.parent, ast.Module):
            return node.name
        return f"{self.__get_fullname(node_link.parent)}.{node.name}"

    @staticmethod
    def __get_docstring(node: ast.Module) -> Optional[str]:
        logger.debug("get docstring: %s", str(node))
        return ast.get_docstring(node)

    @ConvMD.add_tag(TAG.beg_co, TAG.end_co)
    def __get_cla_docstring(self, node: ast.ClassDef) -> Optional[str]:
        return ast.get_docstring(node)

    @ConvMD.repl_beg_end(TAG.beg_str, TAG.end_str, TAG.quote, TAG.html_cr)
    @ConvMD.repl_beg_end(TAG.beg_str, TAG.end_strh, TAG.beg_b, TAG.end_bh)
    @ConvMD.repl_str(TAG.tab, TAG.html_tab)
    @ConvMD.add_tag(TAG.cr, TAG.cr)
    def __get_func_docstring(self, node: ast.FunctionDef) -> Optional[str]:
        logger.debug("get func docstring: %s", str(node.name))
        return ast.get_docstring(node)

    def __get_func_title(self, node: ast.FunctionDef) -> str:
        logger.debug("get func title: %s", str(node.name))
        fullname = self.__get_fullname(node)
        if "@property" in self.__get_decorator(node):
            printname = f"@Property {fullname}"
        else:
            printname = f"{fullname}()"
        self.__add_toc(printname)
        return f"{'#' * (self.__link_lst[node].level + 3)} {printname}"

    @staticmethod
    def __get_func_return(node: ast.FunctionDef) -> str:
        if isinstance(node.returns, ast.Name):
            return " -> " + node.returns.id
        if isinstance(node.returns, ast.Constant):
            return " -> " + str(node.returns.value)
        if (isinstance(node.returns, ast.Attribute)
                and isinstance(node.returns.value, ast.Name)):
            return " -> " + node.returns.value.id + "." + \
                node.returns.attr
        return ""

    @ConvMD.add_tag(TAG.beg_py, TAG.end_py)
    def __get_func_def(self, node: ast.FunctionDef) -> str:
        decorator: str = ""
        logger.debug("get func def: %s", node.name)
        if hasattr(node, "decorator_list"):
            decorator_lst: list[str] = self.__get_decorator(node)
            decorator = "{}\n".format(
                '\n'.join(decorator_lst)) if len(decorator_lst) > 0 else ""
        return f"{decorator}def {self.__get_fullname(node)}" +\
            f"{self.__get_args(node)}{self.__get_func_return(node)}:"

    def __get_cla_title(self, node: ast.ClassDef) -> str:
        logger.debug("get cla title: %s", node.name)
        fullname = f"{node.name}()"
        self.__add_toc(fullname)
        return f"{'#' * (self.__link_lst[node].level + 3)} {fullname}"

    @ConvMD.add_tag(TAG.beg_py, TAG.end_py)
    def __get_cla_def(self, node: ast.ClassDef) -> str:
        logger.debug("get cla def: %s", node.name)
        return f"class {node.name}{self.__get_inheritance(node)}:"

    @staticmethod
    def __get_inheritance(node: ast.ClassDef) -> str:
        inher: list = []
        for base in node.bases:
            if hasattr(base, "id"):
                inher.append(base.id)
        return f"({', '.join(inher)})"

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """
        This function is automatically called by AST mechanisme
        when the current node is a class.
        We update self.output.

        Args:
            node (ast): current node

        Returns:
            None.
        """
        logger.info("visit class: %s", node.name)
        self.__output.extend(
            (
                self.__get_cla_title(node),
                self.__get_cla_def(node),
                self.__get_cla_docstring(node)
            )
        )
        self.generic_visit(node)

    def __valid_name(self, node: ast.FunctionDef) -> bool:
        fullname = self.__get_fullname(node)
        if fullname in self.__func or fullname in BLACKLIST:
            return False
        self.__func.append(fullname)
        return True

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        This function is automatically called by AST mechanisme
        when the current node is a function.
        We update self.output.

        Args:
            node (ast.AST): current node

        Returns:
            None.
        """
        logger.info("visit function: %s", node.name)
        logger.debug("function details: %s", str(ast.dump(node)))

        if self.__priv or node.name.startswith("__") is not True:
            if self.__valid_name(node):
                self.__output.extend(
                    (
                        self.__get_func_title(node),
                        self.__get_func_def(node),
                        self.__get_func_docstring(node)
                    )
                )

        self.generic_visit(node)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
