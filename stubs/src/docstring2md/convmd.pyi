from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

class ConvMD:
    @staticmethod
    def repl_str(old_string: str, new_string: str) -> Callable[[F], F]: ...
    @staticmethod
    def repl_beg_end(begin_regexp: str, end_regexp: str, begin_tag: str, end_tag: str) -> Callable[[F], F]: ...
    @staticmethod
    def add_tag(begin_tag: str, end_tag: str) -> Callable[[F], F]: ...
