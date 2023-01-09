from typing import ParamSpec, Callable

P = ParamSpec('P')

class ConvMD:
    @staticmethod
    def repl_str(old_string: str, new_string: str) -> Callable[[Callable[P, str]], Callable[P, str]]: ...
    @staticmethod
    def repl_beg_end(begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str) -> Callable[[Callable[P, str]], Callable[P, str]]: ...
    @staticmethod
    def add_tag(begin_tag: str, end_tag: str) -> Callable[[Callable[P, str]], Callable[P, str]]: ...
