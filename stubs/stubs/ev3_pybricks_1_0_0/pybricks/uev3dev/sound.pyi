
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Mixer:
    def close() -> None: ...
    def set_beep_volume() -> None: ...
    def set_pcm_volume() -> None: ...
class PCM:
    def close() -> None: ...
    def play() -> None: ...
class PlayType: ...
class Sound:
    def _beep() -> None: ...
    def _play_tone() -> None: ...
    def _stop() -> None: ...
    def play_file() -> None: ...
    def play_note() -> None: ...
    def play_tone() -> None: ...
    def stop() -> None: ...
class SoundFile:
    def _cancel_token() -> None: ...
    def close() -> None: ...
class SoundFileError: ...
class Timeout:
    def _run() -> None: ...
    def cancel() -> None: ...
    def close() -> None: ...
    def start() -> None: ...
    def wait() -> None: ...
    def cancel() -> None: ...
def addressof() -> None: ...
def calcsize() -> None: ...
def debug_print() -> None: ...
def pack() -> None: ...
def sizeof() -> None: ...
def sleep() -> None: ...
def sleep_ms() -> None: ...
class struct: ...
def unpack() -> None: ...