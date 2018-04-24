#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

____                 _        _             ____  __  __ ____
|  _ \  ___   ___ ___| |_ _ __(_)_ __   __ _|___ \|  \/  |  _ \
| | | |/ _ \ / __/ __| __| '__| | '_ \ / _` | __) | |\/| | | | |
| |_| | (_) | (__\__ \ |_| |  | | | | | (_| |/ __/| |  | | |_| |
|____/ \___/ \___|___/\__|_|  |_|_| |_|\__, |_____|_|  |_|____/
                                       |___/

"""

import inspect
import importlib.util
from functools import wraps
import re
import pathlib
import sys


class MyConst:
    docstring_empty = "<b>- docstring empty -</b>"
    head_tag = "#"
    dev_head = "## Dev notes"
    dev_runtime = "### Runtime"
    dev_requirement = "### Requirements"
    decorator_tag = '@'
    function_tag = 'def '
    property_tag = '@Property'


class LineType:
    decorator = 1
    function = 2
    other = 3


class Tag:
    beg_co = "\n```\n"
    end_co = "\n```\n"
    beg_py = "\n```python\n"
    end_py = "\n```\n"
    beg_str = "^"
    end_str = "$"
    end_strh = ":$"
    beg_b = "<b>"
    end_b = "</b>"
    end_bh = ":</b>"
    tab = "    "
    html_tab = "&nbsp;" * 15 + "  "
    cr = "\n"
    html_cr = "<br />"
    quote = "> "


class ConvMD(object):
    """
    Prepare MD string
    """

    def repl_str(old_string, new_string):
        """
        Decorator - search & replace a string by another string
        Example : replace space by a HTML tag.

        Args:
            old_string (str): string to search
            new_string (str): new string

        Returns:
            decorated function

        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return (func(*args, **kwargs)).replace(old_string, new_string)
            return func_wrapper
        return tags_decorator

    def repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag):
        """
        Decorator - replace the beggining and the end

        Example:
            All new lines must be provided with a specific tag
            > 'Line' <br />

        Args:
            begin_regexp (str)
            end_regexp (str)
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function
        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return re.sub(
                    begin_regexp + '(.*)' + end_regexp,
                    begin_tag + r'\1' + end_tag,
                    func(*args, **kwargs),
                    flags=re.MULTILINE
                )
            return func_wrapper
        return tags_decorator

    def add_tag(begin_tag, end_tag):
        """
        Decorator - add a tag

        Example:
            ('__', '__') => __ TXT __

        Args:
            beg_tag (str)
            end_tag (str)

        Returns:
            decorated function
        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(self, *args):
                """ wrapper """
                return "{0}{1}{2}".format(
                    begin_tag, func(self, *args), end_tag)
            return func_wrapper
        return tags_decorator


class TitleObj(object):
    """
    String to store and prepare MD title
    This object will become an attribute.
    """

    def __init__(self, title, level):
        """
        Init => store the sting in value and level (H1/H2/H3/...)
        """
        self.title = title
        self.level = level

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            raise ValueError("TitleObj: Title type is string")

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if isinstance(level, int):
            self.__level = level
        else:
            raise ValueError("TitleObj: level type is int")

    def __repr__(self):
        """
        Provide the MD string according to the level
        """
        return "{} {}".format(MyConst.head_tag * (self.__level + 2),
                              self.__title)

    def __str__(self):
        return repr(self)


class PythonDefinitionObj(object):
    """
    String so store and prepare the object definition:
    Example : def function_name(*args)
    This object will become an attribute.
    """

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, str) and value is not "":
            self.__value = value
        else:
            raise ValueError("PythonDefinitionObj: bad value")

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
    This object will become an attribute.
    """

    def __init__(self, value):
        """
        Store the docstring
        """
        self.value = value

    @property
    def value(self):
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
    def __repr__(self):
        """
        Provide the new docstring with MD tags.
        """
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
        return sorted(self.__members)

    def items(self):
        return self.__members


class PythonObj(object):
    """
    Class in order to register object informations
    __str__ is used to export with MD format.
    """
    def __init__(self, name, full_name, docstring, level):
        self.__title = TitleObj(name, level)
        self.__definition = PythonDefinitionObj(full_name)
        self.__docstring = DocStringObj(docstring)
        self.members = MembersObj()

    def __repr__(self):
        return "\n\n{}\n{}\n{}".format(self.__title,
                                       self.__definition,
                                       self.__docstring
                                       )

    def __str__(self):
        return repr(self)


class ReadFile(object):
    def __init__(self, filename):
        self.filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        """
        check the path to the json file
        Store the path

        Args:
            filename(str): /path/to/the/file

        Returns:
            None

        Raises:
            IOError: File not found
            IOError: File not readable

        """
        if filename is None:
            self.__filename = None
            return
        if pathlib.Path(filename).exists():
            self.__filename = filename
        else:
            raise IOError("File not found ! ({})".format(filename))

    def isdefined(self):
        if self.__filename is None:
            return False
        return True

    def get(self):
        """
        open & read the file
        Returns the content
        """
        current_file = open(self.__filename, "r")
        if current_file.mode == 'r':
            result = current_file.read()
        else:
            raise IOError("File not readable ! ({})".format(filename))
        return result

    def __repr__(self):
        return self.get()

    def __str__(self):
        return repr(self)


class ModuleObj(PythonObj):
    """
    Class in order to register module informations
    __str__ is used to export with MD format.
    """
    def __init__(self, name, full_name, docstring, level=0):
        PythonObj.__init__(self, name, full_name, docstring, level)
        self.__module_docstring = docstring

    def __repr__(self):
        return "{}\n{}\n".format(self.__module_docstring, MyConst.dev_head)

    def __str__(self):
        return repr(self)

    def getallstr(self, member=None):
        output = ""
        if member is None:
            """ First member (Module) """
            member = self
        else:
            """ Children => take the str() """
            output = str(member)
        for idmember in member.members.sortkeys():
            output += self.getallstr(member.members[idmember])
        return output


class ExtractPythonModule(object):
    """
    Object in order to extract Python functions, classes....
    """

    def __init__(self, module_name):
        """
        Init
        """
        self.__module_name = module_name
        self.__module = None
        self.__module_spec = None
        self.module = None

    def __check_module(func):
        """
        Decorator - Checks if module can be imported.
        Updates self.__module_spec in order to import the module.

        Args:
            None

        Retuns:
            bool: The return value. True for success, False otherwise.

        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            self.__module_spec = importlib.util.find_spec(
                self.__module_name)
            if self.__module_spec is None:
                raise Exception("This file is not a module: {}".format(
                    self.__module_name))
            return func(self, *args, **kwargs)
        return wrapper

    @__check_module
    def import_module(self):
        """
        Check module
        Import the module via the passed in module specification
        Returns the newly imported module and updates attributes self.__module

        Args:
            None

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        try:
            self.__module = importlib.util.module_from_spec(self.__module_spec)
            self.__module_spec.loader.exec_module(self.__module)
        except Exception as e:
            raise Exception("Import error")
        return True

    def extract(self):
        """
        Defines module object and extracts all members.

        Args:
            None

        Returns:
            None
        """

        self.module = ModuleObj(self.__module_name,
                                self.__module_name,
                                inspect.getdoc(self.__module))
        self.__extract(self.module, self.__module)

    def __findinline(self, line, search_item):
        if line.find(search_item) is 0:
            return True
        return False

    def __linetype(self, line):
        if self.__findinline(line, MyConst.decorator_tag):
            return LineType.decorator
        if self.__findinline(line, MyConst.function_tag):
            return LineType.function
        return LineType.other

    def __extractdecorator(self, member):
        sourcelines = inspect.getsourcelines(member[1])[0]
        decorator = ""
        result = dict()
        add_decorator = False
        for i, line in enumerate(sourcelines):
            line = line.strip()
            line_type = self.__linetype(line)

            if line_type is LineType.other:
                decorator = ""
                add_decorator = False
            if line_type is LineType.decorator:
                decorator += "{}\n".format(line)
                add_decorator = True
            if line_type is LineType.function:
                if add_decorator:
                    line = line.replace(MyConst.function_tag,
                                        "{}{}.".format(MyConst.function_tag,
                                                       member[0]))
                    result[line] = decorator
        return result

    def __extractproperties(self, my_pythonobj, inspectmembers,
                            level, decorator, cls_name):
        if level >= 2 or len(inspectmembers) is 0:
            return

        level += 1

        for current_property, inspect_obj in inspectmembers:
            full_name = ""
            name = ""
            for current_func in decorator.keys():
                if "{}{}.{}(".format(MyConst.function_tag,
                                     cls_name,
                                     current_property) in current_func:
                    full_name += "{}{}\n".format(decorator[current_func],
                                                 current_func
                                                 )
            name = "{}: {}".format(MyConst.property_tag, current_property)
            new_pythonobj = PythonObj(name,
                                      full_name,
                                      MyConst.property_tag,
                                      level)
            my_pythonobj.members[name] = new_pythonobj

    def __extract(self, my_pythonobj, inspectmembers, level=0, decorator=None):
        """
        Inspects classes & functions in a moddule.
        Store information in a PythonObj object.

        Args:
            inspectmembers (obj): inspect obect
            my_pythonobj (PythonObj): object to define a Python member

        Returns:
            None
        """
        if level >= 2:
            return

        level += 1

        for member in inspect.getmembers(inspectmembers):
            if inspect.isclass(member[1]) and member[0] != "__class__":
                decorator = self.__extractdecorator(member)
                properties = inspect.getmembers(member[1],
                                                lambda o: isinstance(o,
                                                                     property
                                                                     )
                                                )
                name = "{0}()".format(str(member[0]))
                full_name = inspect.getsourcelines(
                        member[1])[0][0].replace('\n', '')
                docstring = inspect.getdoc(member[1])
                new_pythonobj = PythonObj(name, full_name, docstring, level)
                my_pythonobj.members[name] = new_pythonobj

                self.__extractproperties(new_pythonobj,
                                         properties,
                                         level,
                                         decorator,
                                         str(member[0]))
                self.__extract(new_pythonobj,
                               member[1],
                               level,
                               decorator)
            if inspect.isfunction(member[1]):
                name = "{0}{1}".format((str(member[1]).split(" "))[1],
                                       str(inspect.signature(member[1])))
                full_name = "{}{}:".format(MyConst.function_tag, name)
                if decorator is not None and full_name in decorator:
                    full_name = "{}{}".format(decorator[full_name], full_name)
                docstring = inspect.getdoc(member[1])
                new_pythonobj = PythonObj(name, full_name, docstring, level)
                my_pythonobj.members[name] = new_pythonobj


class DocString2MD(object):

    """
    Class DocString2MD : export Google docstring to MD File.
    """

    def __init__(self, module_name, export_file=None, runtime_file=None,
                 requirements_file=None):
        """Init the class
        This function define default attributs.

        Args:
            module_name (str): /path/to/the/module/
            export_file (str): /path/to/the/doc/file - None by default

        Attributes:
            self.__export_file (str): /path/to/the/doc/file - None by default
            self.__my_module
            self.__output

        Returns:
            obj

        """
        self.__runtime = ReadFile(runtime_file)
        self.__requirements = ReadFile(requirements_file)
        self.__export_file = export_file
        self.module_name = module_name
        self.__my_module = ExtractPythonModule(self.module_name)
        self.__output = ""

    @property
    def module_name(self):
        """
        return /path/to/the/json/file

        Args:
            None

        Returns:
            None

        """
        return self.__module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        check the path to the module
        Store the path

        Args:
            module_name(str): /path/to/the/module

        Returns:
            None
        """
        module_name = pathlib.Path(module_name).resolve()
        if pathlib.Path(module_name).exists():
            sys.path.append(module_name.parents[0])
            self.__module_name = module_name.stem
        else:
            raise IOError("Module not found ! ({})".format(module_name))

    def import_module(self):
        if self.__my_module.import_module():
            self.__my_module.extract()
            self.__output = ""
            """ module / README """
            self.__output += str(self.__my_module.module)
            """ runtime """
            if self.__runtime.isdefined():
                self.__output += "{}\n{}{}{}".format(MyConst.dev_runtime,
                                                     Tag.beg_co,
                                                     self.__runtime,
                                                     Tag.end_co
                                                     )
            """ requirements """
            if self.__requirements.isdefined():
                self.__output += "{}\n{}{}{}".format(MyConst.dev_requirement,
                                                     Tag.beg_co,
                                                     self.__requirements,
                                                     Tag.end_co
                                                     )
            """ children """
            self.__output += self.__my_module.module.getallstr()
            return True
        else:
            return False

    def get_doc(self):
        """

        Extract the doc
        Returns self.__output or self.__writedoc

        Args:
            None

        Returns:
            str: self.__output
        """

        if self.__export_file is None:
            return self.__output
        else:
            return self.__writedoc()

    def __writedoc(self):
        """
        Writes the content in the file

        args:
            None

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        try:
            export_file = open(self.__export_file, "w")
            try:
                export_file.write(self.__output)
            finally:
                export_file.close()
        except IOError:
            print("Unable to create {0} on disk.".format(self.__export_file))
            return False

        return True
