from __future__ import annotations
from typing import Generic, TypeVar, Literal

K = Literal["k", "K"]
_T = TypeVar('_T', str, int, float)

# 偶数か奇数であるかを返します
def evenodd(number:int):
    if number%2 == 0:
        return "even"
    else:
        return "odd"

# 偶数かどうかを返します
def iseven(number:int):
    if number%2 == 0:
        return True
    else:
        return False

# 奇数かどうかを返します
def isodd(number:int):
    if number%2 == 0:
        return False
    else:
        return True

# FloatをIntに変換します
def ConvainerforInt(number:float):
    return int(number)

# IntをFloatに変換します
def ConvainerforFloat(number:int):
    return float(number)

# 0より大きい数かを返します
def IsHighfor0(number:int):
    if number > 0:
        return True
    else:
        return False

# 0より小さい数かを返します
def IsLowfor0(number:int):
    if number < 0:
        return True
    else:
        return False

class k(Generic[_T]):
    def __init__(self, num:k):
        self.int = num
        self.integer:k = str(num) + "k"
        if type(num) == str:
            raise TypeError("k indices must be integers")
    
    def __int__(self) -> int:
        return self.int * 1000
    
    def __str__(self) -> str:
        return str(self.integer)
    
    def getk(self) -> str:
        return str(self.integer)
    
    def value(self) -> str:
        return str(self.int * 1000)

testkc = k(20)
print(testkc.value())