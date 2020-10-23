
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Editor:
    def clear_to_eol() -> None: ...
    def cursor() -> None: ...
    def delete_lines() -> None: ...
    def display_window() -> None: ...
    def edit_loop() -> None: ...
    def find_in_file() -> None: ...
    def get_file() -> None: ...
    def get_input() -> None: ...
    def get_screen_size() -> None: ...
    def goto() -> None: ...
    def handle_edit_keys() -> None: ...
    def hilite() -> None: ...
    def line_edit() -> None: ...
    def line_range() -> None: ...
    def mouse_reporting() -> None: ...
    def packtabs() -> None: ...
    def put_file() -> None: ...
    def rd() -> None: ...
    def rd_any() -> None: ...
    def redraw() -> None: ...
    def scroll_down() -> None: ...
    def scroll_region() -> None: ...
    def scroll_up() -> None: ...
    def spaces() -> None: ...
    def undo_add() -> None: ...
    def wr() -> None: ...
def expandtabs() -> None: ...
def pye() -> None: ...
