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

