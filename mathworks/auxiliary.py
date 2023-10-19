# 偶数か奇数であるかを返します
def evenodd(number:int):
    evens: str = ""
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
