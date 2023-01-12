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

import re
from functools import wraps
from typing import Callable, TypeVar, Any, cast

F = TypeVar('F', bound=Callable[..., Any])


class ConvMD:
    """
    Prepare MD string
    """
    @staticmethod
    def repl_str(old_string: str, new_string: str) -> Callable[[F], F]:
        """
        Decorator - search & replace a string by another string
        Examples: replace space by an HTML tag.

        Args:
                    old_string (str): string to search
                    new_string (str): new string

        Returns:
                    Callable[[F], F]

        Examples:

                    >>> from docstring2md.convmd import ConvMD
                    >>> @ConvMD.repl_str("docstring", "is ok !")
                    ... def return_test() -> str:
                    ...     return "my function docstring"
                    >>> print(return_test())
                    my function is ok !

        """
        def tags_decorator(func: F) -> F:
            """ decorator """
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """ wrapper """
                return (func(*args, **kwargs)).replace(old_string, new_string)
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def repl_beg_end(
            begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str)\
            -> Callable[[F], F]:
        """
        Decorator - replace the beginning and the end.

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

                    >>> from docstring2md.convmd import ConvMD
                    >>> @ConvMD.repl_beg_end("^", "$", ">", "<br />")
                    ... def return_test() -> str:
                    ...     return "my function docstring"
                    >>> print(return_test())
                    >my function docstring<br />

        """
        def tags_decorator(func: F) -> F:
            """ decorator """
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """ wrapper """
                return re.sub(
                    begin_regexp + '(.*)' + end_regexp,
                    begin_tag + r'\1' + end_tag,
                    func(*args, **kwargs),
                    flags=re.MULTILINE)
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def add_tag(begin_tag: str, end_tag: str) -> Callable[[F], F]:
        """
        Decorator - add a tag

        Args:
                    begin_tag (str)
                    end_tag (str)

        Returns:
                    decorated function

        Examples:
                    ('__', '__') => __ TXT __

                    >>> from docstring2md.convmd import ConvMD
                    >>> @ConvMD.add_tag("__", "__")
                    ... def return_test() -> str:
                    ...     return "test"
                    >>> print(return_test())
                    __test__

        """
        def tags_decorator(func: F) -> F:
            """ decorator """
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """ wrapper """
                return f"{begin_tag}{func(*args, **kwargs)}{end_tag}"
            return cast(F, func_wrapper)
        return tags_decorator
