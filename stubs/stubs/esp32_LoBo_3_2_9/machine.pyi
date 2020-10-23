
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class ADC:
    def atten() -> None: ...
    def read() -> None: ...
    def readraw() -> None: ...
    def vref() -> None: ...
    def width() -> None: ...
class DAC:
    def write() -> None: ...
class DHT:
    def read() -> None: ...
    def readinto() -> None: ...
class I2C:
    def address() -> None: ...
    def begin() -> None: ...
    def callback() -> None: ...
    def deinit() -> None: ...
    def end() -> None: ...
    def getdata() -> None: ...
    def init() -> None: ...
    def read_byte() -> None: ...
    def read_bytes() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def scan() -> None: ...
    def setdata() -> None: ...
    def slavewrite() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write_byte() -> None: ...
    def write_bytes() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
class Neopixel:
    def HSBtoRGB() -> None: ...
    def HSBtoRGBint() -> None: ...
    def RGBtoHSB() -> None: ...
    def brightness() -> None: ...
    def clear() -> None: ...
    def color_order() -> None: ...
    def deinit() -> None: ...
    def get() -> None: ...
    def info() -> None: ...
    def rainbow() -> None: ...
    def set() -> None: ...
    def setHSB() -> None: ...
    def setHSBint() -> None: ...
    def setWhite() -> None: ...
    def show() -> None: ...
    def timings() -> None: ...
class Onewire:
    def crc8() -> None: ...
    def deinit() -> None: ...
    def readbyte() -> None: ...
    def readbytes() -> None: ...
    def reset() -> None: ...
    def rom_code() -> None: ...
    def scan() -> None: ...
    def search() -> None: ...
    def writebyte() -> None: ...
    def writebytes() -> None: ...
class PWM:
    def deinit() -> None: ...
    def duty() -> None: ...
    def freq() -> None: ...
    def init() -> None: ...
    def list() -> None: ...
    def pause() -> None: ...
    def resume() -> None: ...
class Pin:
    def init() -> None: ...
    def irq() -> None: ...
    def value() -> None: ...
class RTC:
    def clear() -> None: ...
    def init() -> None: ...
    def now() -> None: ...
    def ntp_state() -> None: ...
    def ntp_sync() -> None: ...
    def read() -> None: ...
    def read_string() -> None: ...
    def synced() -> None: ...
    def wake_on_ext0() -> None: ...
    def wake_on_ext1() -> None: ...
    def write() -> None: ...
    def write_string() -> None: ...
class SPI:
    def deinit() -> None: ...
    def deselect() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readfrom_mem() -> None: ...
    def readinto() -> None: ...
    def select() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...
class Signal:
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...
class Timer:
    def callback() -> None: ...
    def deinit() -> None: ...
    def events() -> None: ...
    def init() -> None: ...
    def isrunning() -> None: ...
    def pause() -> None: ...
    def period() -> None: ...
    def reshot() -> None: ...
    def resume() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def timernum() -> None: ...
    def value() -> None: ...
class TouchPad:
    def config() -> None: ...
    def read() -> None: ...
class UART:
    def any() -> None: ...
    def callback() -> None: ...
    def flush() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def readln() -> None: ...
    def write() -> None: ...
def deepsleep() -> None: ...
def disable_irq() -> None: ...
def enable_irq() -> None: ...
def freq() -> None: ...
def heap_info() -> None: ...
def idle() -> None: ...
def internal_temp() -> None: ...
def loglevel() -> None: ...
def nvs_erase() -> None: ...
def nvs_erase_all() -> None: ...
def nvs_getint() -> None: ...
def nvs_getstr() -> None: ...
def nvs_setint() -> None: ...
def nvs_setstr() -> None: ...
def random() -> None: ...
def redirectlog() -> None: ...
def reset() -> None: ...
def restorelog() -> None: ...
def stdin_disable() -> None: ...
def stdin_get() -> None: ...
def stdout_put() -> None: ...
def time_pulse_us() -> None: ...
def unique_id() -> None: ...
def wake_description() -> None: ...
def wake_reason() -> None: ...
