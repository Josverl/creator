
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Epoll:
    def close() -> None: ...
    def poll() -> None: ...
    def poll_ms() -> None: ...
    def register() -> None: ...
    def unregister() -> None: ...
def epoll() -> None: ...
def poll() -> None: ...
