#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####    ####   #    #  ######     #     ####
 #    #  #    #  ##   #  #          #    #    #
 #       #    #  # #  #  #####      #    #
 #       #    #  #  # #  #          #    #  ###
 #    #  #    #  #   ##  #          #    #    #
  ####    ####   #    #  #          #     ####

"""


CONST = {
    "docstring_empty": "Docstring empty",
    "head_tag": "#",
    "dev_head": "## Dev notes",
    "dev_runtime": "### Runtime",
    "dev_requirement": "### Requirements",
    "dev_uml": "### UML Diagram",
    "dev_obj": "### Objects",
    "decorator_tag": '@',
    "function_tag": 'def ',
    "property_tag": '@Property',
}

BLACKLIST = ["wrapper"]

TAG = {
    "beg_co": "\n```\n",
    "end_co": "\n```\n",
    "beg_py": "```python\n",
    "end_py": "\n```",
    "beg_str": "^",
    "end_str": "$",
    "end_strh": ":$",
    "beg_b": "<b>",
    "end_b": "</b>",
    "end_bh": ":</b>",
    "tab": "    ",
    "html_tab": "&nbsp;" * 15 + "  ",
    "cr": "\n",
    "html_cr": "<br />",
    "quote": "> "
}
