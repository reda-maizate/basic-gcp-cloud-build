from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    if type(a) == str or type(b) == str:
        raise TypeError("Cannot add strings")
    return a + b
