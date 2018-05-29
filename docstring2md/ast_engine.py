#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""

   #     #####  #######
  # #   #     #    #
 #   #  #          #
#     #  #####     #
#######       #    #
#     # #     #    #
#     #  #####     # engine

"""
import ast
import re
from docstring2md import TAG, BLACKLIST
from docstring2md import ConvMD
from docstring2md.log import PytLog


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
        >>> from docstring2md.file import PytFile
        >>> import pathlib
        >>> module = str(pathlib.Path(__file__).resolve())
        >>> source = PytFile(module)
        >>> # init
        >>> doc = ObjVisitor(module_docstring=False)
        >>> # provide source, generate the tree and use visit mechanisme
        >>> doc.visit(doc.get_tree(source.read()))
        >>> result = doc.output
        >>> result = result.split("\\n")
        >>> result[0]
        '#### ObjVisitor()'
        >>> result = doc.toc
        >>> result = result.split("\\n")
        >>> result[0]
        '[ObjVisitor()](#objvisitor)<br />'
    """
    def __init__(self, module_docstring=False, priv=False, debug=False):
        super(ast.NodeVisitor, self).__init__()
        self.__log = PytLog()
        self.__debug = debug
        if self.__debug:
            self.__log.set_debug()
        self.__toc = []
        self.__output = []
        self.__module_docstring = module_docstring
        self.__priv = priv
        self.__func = []

    @property
    def toc(self):
        return "\n".join(self.__toc)

    @property
    def output(self):
        return "\n".join(self.__output)

    def get_tree(self, source):
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

    def visit_Module(self, node):
        """
        This function is automatically called by AST mechanisme
        when the current node is a module.
        We update self.output.

        Args:
            node (ast): current node

        Returns:
            None.
        """
        self.__log.info("visit module: {}".format(node))
        if self.__module_docstring:
            self.__output.append(self.__get_docstring(node))
        self.generic_visit(node)

    def __set_parent(self, node):
        if hasattr(node, "level") is not True:
            node.level = 0
        for child in ast.iter_child_nodes(node):
            child.parent = node
            child.level = int(node.level) + 1

    def __add_toc(self, title):
        anchor = str(title)
        anchor = re.sub(r"__([a-zA-Z_]*)__\(", r"\1(", anchor)
        anchor = re.sub(
            r"[^\w\- ]+", "", (anchor.replace(' ', '-')).lower())
        self.__toc.append("[{}](#{})<br />".format(title, anchor))

    def __get_args(self, node):
        argument = []
        for arg in node.args.args:
            argument.append(arg.arg)

        idx = len(argument) - len(node.args.defaults)
        for arg in node.args.defaults:
            value = "unknown"
            # print(ast.dump(arg))
            if isinstance(arg, ast.Num):
                value = arg.n
            if isinstance(arg, ast.Str):
                value = arg.s
            if isinstance(arg, ast.NameConstant):
                value = arg.value
            argument[idx] = argument[idx] + "=" + str(value)
            idx += 1
        if hasattr(node.args.vararg, "arg"):
            argument.append("*{}".format(node.args.vararg.arg))
        if hasattr(node.args.kwarg, "arg"):
            argument.append("**{}".format(node.args.kwarg.arg))

        return "({})".format(', '.join(argument))

    def __get_decorator_args(self, node):
        args = []
        for attribute in node.args:
            if isinstance(node.func, ast.Name):
                attribute_id = attribute.id
            else:
                attribute_id = attribute.value.id
            attribute_attr = ""
            if hasattr(attribute, "attr"):
                attribute_attr = "." + attribute.attr

            args.append(attribute_id + attribute_attr)

        return "({})".format(', '.join(args))

    def __get_decorator(self, node):
        decorator = []
        for dec in node.decorator_list:
            name = ''
            if isinstance(dec, ast.Name):
                name = dec.id
            elif isinstance(dec, ast.Attribute):
                name = dec.attr
            elif isinstance(dec, ast.Call):
                if isinstance(dec.func, ast.Attribute):
                    name = dec.func.value.id
                else:
                    name = dec.func.id
                if hasattr(dec.func, "attr"):
                    name = ".".join(name, dec.func.attr)
                if hasattr(dec, "args"):
                    self.__get_decorator_args(dec)
                    name += self.__get_decorator_args(dec)
            decorator.append("@" + name)

        return decorator

    def __get_fullname(self, node):
        if hasattr(node, "parent"):
            return "{}.{}".format(
                self.__get_fullname(node.parent),
                node.name
            )
        else:
            return node.name

    def __get_docstring(self, node):
        self.__log.debug("get docstring: {}".format(node))
        return ast.get_docstring(node)

    @ConvMD.add_tag(TAG["beg_co"], TAG["end_co"])
    def __get_cla_docstring(self, node):
        return ast.get_docstring(node)

    @ConvMD.repl_beg_end(
        TAG["beg_str"], TAG["end_str"], TAG["quote"], TAG["html_cr"]
    )
    @ConvMD.repl_beg_end(
        TAG["beg_str"], TAG["end_strh"], TAG["beg_b"], TAG["end_bh"]
    )
    @ConvMD.repl_str(TAG["tab"], TAG["html_tab"])
    @ConvMD.add_tag(TAG["cr"], TAG["cr"])
    def __get_func_docstring(self, node):
        self.__log.debug("get func docstring: {}".format(node.name))
        return ast.get_docstring(node)

    def __get_func_title(self, node):
        self.__log.debug("get func title: {}".format(node.name))
        fullname = self.__get_fullname(node)
        if "@property" in self.__get_decorator(node):
            printname = "@Property {}".format(fullname)
        else:
            printname = "{}()".format(fullname)
        self.__add_toc("{}".format(printname))
        return "{} {}".format(
            "#" * (int(node.level) + 4),
            printname
        )

    @ConvMD.add_tag(TAG["beg_py"], TAG["end_py"])
    def __get_func_def(self, node):
        self.__log.debug("get func def: {}".format(node.name))
        if hasattr(node, "decorator_list"):
            decorator = self.__get_decorator(node)
        return "{}\ndef {}{}:".format(
            '\n'.join(decorator),
            self.__get_fullname(node),
            self.__get_args(node)
        )

    def __get_cla_title(self, node):
        self.__log.debug("get cla title: {}".format(node.name))
        fullname = "{}()".format(node.name)
        self.__add_toc(fullname)
        return "{} {}".format(
            "#" * (int(node.level) + 4),
            fullname
        )

    @ConvMD.add_tag(TAG["beg_py"], TAG["end_py"])
    def __get_cla_def(self, node):
        self.__log.debug("get cla def: {}".format(node.name))
        return "class {}{}:".format(
            node.name,
            self.__get_inheritance(node)
        )

    def __get_inheritance(self, node):
        inher = []
        for base in node.bases:
            if hasattr(base, "id"):
                inher.append(base.id)
        return "({})".format(', '.join(inher))

    def visit_ClassDef(self, node):
        """
        This function is automatically called by AST mechanisme
        when the current node is a class.
        We update self.output.

        Args:
            node (ast): current node

        Returns:
            None.
        """
        self.__log.info("visit class: {}".format(node.name))
        self.__set_parent(node)
        self.__output.extend(
            (
                self.__get_cla_title(node),
                self.__get_cla_def(node),
                self.__get_cla_docstring(node)
            )
        )
        self.generic_visit(node)

    def __valid_name(self, node):
        fullname = self.__get_fullname(node)
        if fullname in self.__func or fullname in BLACKLIST:
            return False
        else:
            self.__func.append(fullname)
            return True

    def visit_FunctionDef(self, node):
        """
        This function is automatically called by AST mechanisme
        when the current node is a function.
        We update self.output.

        Args:
            node (ast): current node

        Returns:
            None.
        """
        self.__log.info("visit function: {}".format(node.name))
        if self.__priv or node.name.startswith("__") is not True:
            self.__set_parent(node)
            if node.level <= 2 and self.__valid_name(node):
                self.__output.extend(
                    (
                        self.__get_func_title(node),
                        self.__get_func_def(node),
                        self.__get_func_docstring(node)
                    )
                )
        else:
            node.disable = True
        self.generic_visit(node)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
