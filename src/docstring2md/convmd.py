#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

from functools import wraps
import re


class ConvMD:
    """
    Prepare MD string
    """
    @staticmethod
    def repl_str(old_string, new_string):
        """
        Decorator - search & replace a string by another string
        Examples: replace space by a HTML tag.

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

    @staticmethod
    def repl_beg_end(begin_regexp: str, end_regexp: str, begin_tag: str,
                     end_tag: str):
        """
        Decorator - replace the beggining and the end

        Args:
            begin_regexp (str)
            end_regexp (str)
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function

        Examples:
            All new lines must be provided with a specific tag
            > 'Line' <br />

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
                    flags=re.MULTILINE)
            return func_wrapper
        return tags_decorator

    @staticmethod
    def add_tag(begin_tag, end_tag):
        """
        Decorator - add a tag

        Args:
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function

        Examples:
            ('__', '__') => __ TXT __

        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args):
                """ wrapper """
                return f"{begin_tag}{func(*args)}{end_tag}"
            return func_wrapper
        return tags_decorator
