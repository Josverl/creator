
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def get_battery_voltage() -> Any: ...
    #   0: return measuredvbat
    # ? 0: return measuredvbat
def get_battery_charging() -> bool: ...
def set_dotstar_power(state: Any) -> None: ...
def dotstar_color_wheel(wheel_pos: Any) -> Union[Tuple[, Any, Any], Tuple[Any, , Any], Tuple[Any, Any, ]]: ...
def go_deepsleep(t: Any) -> None: ...
