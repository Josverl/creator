# make_stub_files: Tue 23 Apr 2019 at 22:52:01

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Editor:
    def __init__(self, tab_size: smallint, undo_limit: Any) -> None: ...
    def wr(self, s: str) -> None: ...
    def rd_any(self) -> bool: ...
    def rd(self) -> Union[Any, str]: ...
        #   0: return sys.stdin.read(1)
        # ? 0: return sys.stdin.read(number)
        #   1: return '\x03'
        #   1: return str
    def goto(self, row: Any, col: Any) -> None: ...
    def clear_to_eol(self) -> None: ...
    def cursor(self, onoff: Any) -> None: ...
    def hilite(self, mode: Any) -> None: ...
    def mouse_reporting(self, onoff: Any) -> None: ...
    def scroll_region(self, stop: Any) -> None: ...
    def scroll_up(self, scrolling: Any) -> None: ...
    def scroll_down(self, scrolling: Any) -> None: ...
    def get_screen_size(self) -> Any: ...
        #   0: return int(i,10) for i in pos.lstrip('\n\x1b[').split(';')
        # ? 0: return int for int in pos.lstrip(str).split(str)
    def redraw(self, flag: Any) -> None: ...
    def get_input(self) -> Union[Tuple[Any, str], Tuple[number, Any, Any, Any], Tuple[number, Any], Tuple[number, str]]: ...
    def display_window(self) -> None: ...
    def spaces(self, line: Any, pos: Any=None) -> int: ...
    def line_range(self) -> Tuple[Any, Any]: ...
    def line_edit(self, prompt: Any, default: Any) -> Optional[Any]: ...
        #   0: return res
        # ? 0: return res
        #   1: return None
        #   1: return None
    def find_in_file(self, pattern: Any, col: Any, end: Any) -> number: ...
    def undo_add(self, lnum: Any, text: Any, key: Any, span: Any=1) -> None: ...
    def delete_lines(self, yank: Any) -> None: ...
    def handle_edit_keys(self, key: Any, char: smallint) -> bool: ...
    def edit_loop(self) -> Any: ...
        #   0: return key
        # ? 0: return key
        #   1: return key
        # ? 1: return key
    def packtabs(self, s: str) -> Any: ...
        #   0: return sb.getvalue()
        # ? 0: return sb.getvalue()
    def get_file(self, fname: Any) -> None: ...
    def put_file(self, fname: Any) -> None: ...
def expandtabs(s: str) -> Union[Any, str]: ...
    #   0: return sb.getvalue()
    # ? 0: return sb.getvalue()
    #   1: return s
    #   1: return str
def pye(*content) -> Any: ...
