from typing import Any


def ccast[T](typ: T, val: Any) -> T:
    """
    cast with runtime check, ccast is short for checked_cast
    """
    if not isinstance(val, typ):
        raise TypeError(
            f"Expected {typ.__name__}, got {val} of type {type(val).__name__}"
        )
    return val
