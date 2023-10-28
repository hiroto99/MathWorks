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
