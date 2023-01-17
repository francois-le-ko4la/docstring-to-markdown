#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docstring2md: convmd.

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
from __future__ import annotations

import html
import re
import textwrap
from functools import wraps
from typing import Any, Callable, TypeVar, cast

from docstring2md.__config__ import Tag

F = TypeVar('F', bound=Callable[..., Any])


class ConvMD:
    """Prepare MD string."""

    @staticmethod
    def repl_str(old_string: str, new_string: str) -> Callable[[F], F]:
        """Search & replace a string by another string.

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
            """Decorate."""
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """Wrapp."""
                return (func(*args, **kwargs)).replace(old_string, new_string)
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def repl_beg_end(
            begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str)\
            -> Callable[[F], F]:
        """Replace the beginning and the end.

        Args:
            begin_regexp (str)
            end_regexp (str)
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function

        Examples:
            >>> # All new lines must be provided with a specific tag
            >>> # > 'Line' <br />
            >>> from docstring2md.convmd import ConvMD
            >>> @ConvMD.repl_beg_end("^", "$", ">", "<br />")
            ... def return_test() -> str:
            ...     return "my function docstring"
            >>> print(return_test())
            >my function docstring<br />

        """
        def tags_decorator(func: F) -> F:
            """Decorate."""
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """Wrapp."""
                return re.sub(
                    begin_regexp + r'(\S.*)' + end_regexp,
                    begin_tag + r'\1' + end_tag,
                    func(*args, **kwargs),
                    flags=re.MULTILINE)
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def add_tag(begin_tag: str, end_tag: str) -> Callable[[F], F]:
        """Add a tag in a string.

        Args:
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function

        Examples:
            >>> # ('__', '__') => __ TXT __
            >>> from docstring2md.convmd import ConvMD
            >>> @ConvMD.add_tag("__", "__")
            ... def return_test() -> str:
            ...     return "test"
            >>> print(return_test())
            __test__

        """
        def tags_decorator(func: F) -> F:
            """Decorate."""
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """Wrapp."""
                return f"{begin_tag}{func(*args, **kwargs)}{end_tag}"
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def html_escape() -> Callable[[F], F]:
        """Escape the HTML Tag.

        Returns:
            decorated function

        """
        def tags_decorator(func: F) -> F:
            """Decorate."""
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """Wrapp."""
                return html.escape(func(*args, **kwargs))
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def colorize_examples() -> Callable[[F], F]:
        """Colorize python example.

        Returns:
            decorated function

        """
        def tags_decorator(func: F) -> F:
            """Decorate."""
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """Wrapp."""
                ret = func(*args, **kwargs)
                if re.search(r"\nExamples:\n", ret):
                    ret = f"{Tag.BEG_PRE.value}{Tag.CR.value}{ret}" + \
                          f"{Tag.CR.value}{Tag.BEG_END_CO.value}"
                    ret = ret.replace(
                        "\nExamples:\n",
                        f"\n{Tag.END_PRE.value}\nExamples:\n" +
                        f"{Tag.BEG_PY.value}{Tag.CR.value}")
                    return ret
                return f"{Tag.BEG_PRE.value}{Tag.CR.value}{ret}" + \
                       f"{Tag.CR.value}"f"{Tag.END_PRE.value}"
            return cast(F, func_wrapper)
        return tags_decorator

    @staticmethod
    def dedent() -> Callable[[F], F]:
        """Deindent text.

        Returns:
            decorated function

        """
        def tags_decorator(func: F) -> F:
            """Decorate."""
            @wraps(func)
            def func_wrapper(*args: Any, **kwargs: Any) -> Any:
                """Wrapp."""
                return textwrap.dedent(func(*args, **kwargs))
            return cast(F, func_wrapper)
        return tags_decorator


if __name__ == "__main__":
    import doctest
    doctest.testmod()
