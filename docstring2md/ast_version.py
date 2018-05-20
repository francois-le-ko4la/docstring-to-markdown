# -*- coding: utf-8 -*-
"""Parse Python source code and get or print docstrings."""

__all__ = ('get_docstrings', 'print_docstrings')

import ast
from itertools import groupby
from os.path import basename, splitext

class FuncLister(ast.NodeVisitor):
    def __init__(self):
        super(ast.NodeVisitor, self).__init__()

    def __set_parent(self, node):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    def __get_args(self, node):
        argument=[]
        for arg in node.args.args:
            argument.append(arg.arg)

        idx = len(argument) - len(node.args.defaults)
        for arg in node.args.defaults:
            value="unknown"
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
        args=[]
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
        decorator=[]
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
                    name = name + "." + dec.func.attr
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
        return ast.get_docstring(node)

    def __get_inheritance(self, node):
        inher=[]
        for base in node.bases:
            inher.append(base.id)
        return "({})".format(', '.join(inher))

    def visit_ClassDef(self, node):
        self.__set_parent(node)
        print("classe {}{}:\n{}".format(
                node.name,
                self.__get_inheritance(node),
                self.__get_docstring(node)
            )
        )
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if node.name.startswith("__") is not True:
            self.__set_parent(node)
            if hasattr(node, "decorator_list"):
                decorator = self.__get_decorator(node)
            print("{}\ndef {}{}:".format(
                    '\n'.join(decorator),
                    self.__get_fullname(node),
                    self.__get_args(node)
                )
            )
            print(self.__get_docstring(node))
        self.generic_visit(node)


def get_docstrings(source, module='<string>'):
    if hasattr(source, 'read'):
        filename = getattr(source, 'name', module)
        module = splitext(basename(filename))[0]
        source = source.read()

    tree = ast.parse(source)
    FuncLister().visit(tree)
    exit()


if __name__ == '__main__':
    import sys
    
    with open(sys.argv[1]) as fp:
        get_docstrings(fp)
