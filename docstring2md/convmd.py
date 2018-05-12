#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

                         #####
 #####    ####    ####  #     #  #    #  #####
 #    #  #    #  #    #       #  ##  ##  #    #
 #    #  #    #  #       #####   # ## #  #    #
 #    #  #    #  #      #        #    #  #    #
 #    #  #    #  #    # #        #    #  #    #
 #####    ####    ####  #######  #    #  #####


"""

from functools import wraps
import re


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
