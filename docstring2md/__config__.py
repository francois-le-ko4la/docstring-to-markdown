#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""


class MyConst:
    docstring_empty = "Docstring empty"
    head_tag = "#"
    dev_head = "## Dev notes"
    dev_runtime = "### Runtime"
    dev_requirement = "### Requirements"
    dev_uml = "### UML Diagram"
    dev_obj = "### Objects"
    decorator_tag = '@'
    function_tag = 'def '
    property_tag = '@Property'


class LineType:
    decorator = 1
    function = 2
    other = 3


class PythonObjType:
    mod = 0
    cla = 1
    fun = 2


class Tag:
    beg_co = "\n```\n"
    end_co = "\n```\n"
    beg_py = "```python\n"
    end_py = "\n```"
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
