
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def _resolve_addr() -> None: ...
def create_connection() -> None: ...
class error: ...
def getaddrinfo() -> None: ...
def inet_aton() -> None: ...
def inet_ntop() -> None: ...
def inet_pton() -> None: ...
def sockaddr() -> None: ...
class socket:
    def close() -> None: ...
    def fileno() -> None: ...
    def listen() -> None: ...
    def makefile() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def recv() -> None: ...
    def recvfrom() -> None: ...
    def send() -> None: ...
    def sendall() -> None: ...
    def setblocking() -> None: ...
    def setsockopt() -> None: ...
    def write() -> None: ...
