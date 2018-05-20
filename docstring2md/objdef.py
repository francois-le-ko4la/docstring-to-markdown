#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

                         #####
 #####    ####    ####  #     #  #    #  #####
 #    #  #    #  #    #       #  ##  ##  #    #
 #    #  #    #  #       #####   # ## #  #    #
 #    #  #    #  #      #        #    #  #    #
 #    #  #    #  #    # #        #    #  #    #
 #####    ####    ####  #######  #    #  #####


"""

from docstring2md.convmd import ConvMD
from docstring2md.__config__ import Tag, MyConst, PythonObjType
import re


class TitleObj(object):

    """
    String to store and prepare MD title
    This object will become an attribute.

    Use:
        >>> title = TitleObj(3, "oups")
        Traceback (most recent call last):
        ...
        ValueError: TitleObj: Title type is string
        >>> title = TitleObj("Test_def(self, var, indx)", 3)
        >>> print(title)
        ###### Test_def(self, var, indx)
        >>> print(title.getanchor())
        test_defself-var-indx
    """

    def __init__(self, title, level):
        """
        Init => store the string in value and level (H1/H2/H3/...)
        """
        self.__title = None
        self.__level = None
        self.title = title
        self.level = level

    @property
    def title(self):
        """
        Store the title
        """
        return self.__title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            raise ValueError("TitleObj: Title type is string")

    @property
    def level(self):
        """
        Store the level
        """
        return self.__level

    @level.setter
    def level(self, level):
        if isinstance(level, int):
            self.__level = level
        else:
            raise ValueError("TitleObj: level type is int")

    def getanchor(self):
        """
        provide a link to prepare the toc.
        """
        anchor = str(self.__title)
        anchor = re.sub(r"__([a-zA-Z_]*)__\(", r"\1(", anchor)
        anchor = re.sub(
            r"[^\w\- ]+", "", (anchor.replace(' ', '-')).lower())
        return anchor

    def __repr__(self):
        """
        Provide the MD string according to the level
        """
        return "{} {}".format(
            MyConst.head_tag * (self.__level + 3),
            self.__title)

    def __str__(self):
        return repr(self)


class PythonDefinitionObj(object):

    """
    String so store and prepare the object definition:
    Example : def function_name(*args)
    This object will become an attribute.

    Use:
        >>> obj = PythonDefinitionObj(1)
        Traceback (most recent call last):
        ...
        ValueError: PytDefObj: bad value
        >>> obj = PythonDefinitionObj("")
        Traceback (most recent call last):
        ...
        ValueError: PytDefObj: bad value
        >>> obj = PythonDefinitionObj("MyOBJ")
        >>> print(obj)
        ```python
        MyOBJ
        ```

    """

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        """
        Store the value
        """
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, str) and value is not "":
            self.__value = value
        else:
            raise ValueError("PytDefObj: bad value")

    @ConvMD.add_tag(Tag.beg_py, Tag.end_py)
    def __repr__(self):
        """
        Provide the definition string with MD tags.
        """
        return self.__value

    def __str__(self):
        """
        Call repr
        """
        return repr(self)


class DocStringObj(object):

    """
    String to store and prepare the docstring.
    This object will become an attribut.

    Use:
        >>> docstring = DocStringObj("My docstring", PythonObjType.fun)
        >>> print(docstring)
        > <br />
        > My docstring<br />
        > <br />
        >>> docstring = DocStringObj("", PythonObjType.fun)
        >>> print(docstring)
        > <br />
        > <br />
        > <br />
        >>> docstring = DocStringObj("My docstring", PythonObjType.cla)
        >>> print(docstring)
        <BLANKLINE>
        ```
        My docstring
        ```
        <BLANKLINE>
    """

    def __init__(self, value, obj_type):
        self.__value = None
        self.value = value
        self.__obj_type = obj_type

    @property
    def value(self):
        """
        Store the docstring
        """
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            value = MyConst.docstring_empty
        if isinstance(value, str):
            self.__value = value
        else:
            raise ValueError("DocStringObj: bad value")

    @ConvMD.repl_beg_end(Tag.beg_str, Tag.end_str, Tag.quote, Tag.html_cr)
    @ConvMD.repl_beg_end(Tag.beg_str, Tag.end_strh, Tag.beg_b, Tag.end_bh)
    @ConvMD.repl_str(Tag.tab, Tag.html_tab)
    @ConvMD.add_tag(Tag.cr, Tag.cr)
    def __repr_fun(self):
        """
        Provide a function docstring with MD tags.
        """
        return self.value

    @ConvMD.add_tag(Tag.beg_co, Tag.end_co)
    def __repr_cla(self):
        """
        Provide a class docstring with MD tags.
        """
        return self.value

    def __repr__(self):
        if self.__obj_type is PythonObjType.fun:
            return self.__repr_fun()
        elif self.__obj_type is PythonObjType.cla:
            return self.__repr_cla()
        else:
            return self.value

    def __str__(self):
        """
        Call repr
        """
        return repr(self)


class MembersObj(object):

    """
    Dict() to store a python object's members.
    This object will become an attribute.
    """

    def __init__(self):
        self.__members = dict()

    def __repr__(self):
        return str(self.__members)

    def __str__(self):
        return repr(self)

    def __setitem__(self, index, value):
        self.__members[index] = value

    def __getitem__(self, index):
        return self.__members[index]

    def __len__(self):
        return len(self.__members)

    def sortkeys(self):
        """
        sort the key before using the list
        """
        return sorted(self.__members)

    def items(self):
        """
        get items
        """
        return self.__members


class PythonObj(object):

    """
    Class in order to register object informations
    __str__ is used to export with MD format.

    Use:
        >>> obj = PythonObj("Mc", "def Mc()", "Doc", 1, PythonObjType.fun)
        >>> print(obj)
        <BLANKLINE>
        #### Mc
        ```python
        def Mc()
        ```
        > <br />
        > Doc<br />
        > <br />
        >>> obj = PythonObj("Mc", "class Mc():", "Doc", 1, PythonObjType.cla)
        >>> print(obj)
        <BLANKLINE>
        #### Mc
        ```python
        class Mc():
        ```
        <BLANKLINE>
        ```
        Doc
        ```
        <BLANKLINE>
    """

    def __init__(self, name, full_name, docstring, level, obj_type):
        self.__title = TitleObj(name, level)
        self.__definition = PythonDefinitionObj(full_name)
        self.__docstring = DocStringObj(docstring, obj_type)
        self.members = MembersObj()

    def getlink(self):
        """
        MD Link format
        """
        return "[{}](#{})<br />\n".format(self.__title.title,
                                          self.__title.getanchor())

    def __repr__(self):
        return "\n{}\n{}\n{}".format(
            self.__title,
            self.__definition,
            self.__docstring
        )

    def __str__(self):
        return repr(self)


class ModuleObj(PythonObj):

    """
    Class in order to register module informations
    __str__ is used to export with MD format.

    Use:
        >>> obj = ModuleObj("Mod", "module", "mod doc")
        >>> print(obj)
        mod doc
        ## Dev notes
        <BLANKLINE>
    """

    def __init__(self, name, full_name, docstring, level=0):
        PythonObj.__init__(self, name, full_name, docstring, level,
                           PythonObjType.mod)
        self.__module_docstring = docstring

    def __repr__(self):
        return "{}\n{}\n".format(self.__module_docstring, MyConst.dev_head)

    def __str__(self):
        return repr(self)

    def gettoc(self, member=None):
        """
        Get all link and provide a toc
        """
        toc = ""
        if member is None:
            member = self
        else:
            toc = member.getlink()
        if len(member.members.sortkeys()) is not 0:
            for idmember in member.members.sortkeys():
                toc += self.gettoc(member.members[idmember])
        return toc

    def getallstr(self, member=None):
        """
        get all definitions and docstring
        """
        output = ""
        if member is None:
            """ First member (Module) """
            member = self
        else:
            """ Children => take the str() """
            output = str(member)
        if len(member.members.sortkeys()) is not 0:
            for idmember in member.members.sortkeys():
                output += self.getallstr(member.members[idmember])
        return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
