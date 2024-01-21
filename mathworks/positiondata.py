from __future__ import annotations
from os import path as os
from typing import (
    Generic,
    Iterator,
    Iterable,
    SupportsInt,
    SupportsIndex,
    TypeVar
)
from typing import (
    overload,
)
from collections.abc import Iterable, Iterator
from mathworks import procotol
import sys as system
import time

P = TypeVar('P')
F = TypeVar('F', str, str)

class pos(Iterable[P], Generic[P]):
    def __init__(self, value):
        if type(value) is list:
            for a in value:
                if type(a) is not tuple or None:
                    text = 'can only concatenate {type} (not "tuple") to {type}'
                    text.format(type=type(a))
                    raise TypeError(text)
                elif type(a) is tuple:
                    if len(a) == 2:
                        for b in a:
                            if type(b) is not int:
                                text = 'can only concatenate {type} (not "int") to {type}'
                                text.format(type=type(b))
                                raise TypeError(text)
                            else:
                                pass
                    else:
                        raise IndexError("list index out of range")
                else:
                    pass
        elif type(value) is None:
            self.value = None
        else:
            text = "pos() argument must be a list, not '{type}'"
            text.format(type=type(value))
            raise TypeError(text)
        self.value = value

    def __hash__(self):
        return hash((self.value))
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __getitem__(self, i: SupportsInt) -> pos[P]:
        if isinstance(i, SupportsInt):
            return self.value[i]
    
    def __setitem__(self, i):
        if type(i) is list:
            for a in i:
                if type(a) is not tuple or None:
                    text = 'can only concatenate {type} (not "tuple") to {type}'
                    text.format(type=type(a))
                    raise TypeError(text)
                elif type(a) is tuple:
                    if len(a) == 2:
                        for b in a:
                            if type(b) is not int:
                                text = 'can only concatenate {type} (not "int") to {type}'
                                text.format(type=type(b))
                                raise TypeError(text)
                            else:
                                pass
                    else:
                        raise IndexError("list index out of range")
                else:
                    pass
        elif type(i) is None:
            self.value = None
        else:
            text = "pos() argument must be a list, not '{type}'"
            text.format(type=type(i))
            raise TypeError(text)
        self.value = i
    
    def __iter__(self) -> Iterator[P]:
        return iter(self.value)
    
    def add(self, __x:int, __y:int) -> pos:
        lists = tuple([__x, __y])
        self.value.append(lists)
        return self.value
    
    def echo(self, plece:int, plece2:int=None, backcall:bool=False) -> str:
        """
            posit.echo(0,0) -> print(posit[0][0])

            echo outputs the index of the position (which is the return value when backcall=true).
        """

        if (backcall == True):
            if (plece2 == None):
                return str(self.value[plece])
            else:
                return str(self.value[plece][plece2])
        else:
            if (plece2 == None):
                print(self.value[plece])
            else:
                print(self.value[plece][plece2])
    
    def clear(self) -> pos:
        """
            clear is delete all position.
        """
        self.value = []
        return self.value
    
    def delete(self, index:int) -> pos:
        self.value.remove(self.value[index])
        return self.value

    def cleanw(self):
        """
            cleanw is remove to same position.
        """
        board = []
        for n in self.value:
            if n in board:
                pass
            else:
                board.append(n)
        self.value = board
        return self.value

    def sort(self, turn:bool):
        """
            sort sorts number.
            When turn=False, sorting is done starting with the smallest number.
            When turn=True, sorting is done starting with the biggest number.
        """
        bound = sorted(self.value, reverse=turn)
        self.value = bound
        return self.value
    
    def find(self, x:int, y:int) -> int:
        bound = (x, y)
        if bound in self.value:
            return self.value.index(bound)
        else:
            return -1

# 座標に関するクラスです
class position():

    # 座標の変数を設定します
    def __init__(self, _x:int, _y:int):
        self._x = _x
        self._y = _y

    # リストを座標の変数に変換します
    def NewPosition(self, pos:list):
        if (pos == None):
            pos = ["?listtype=__pos__"]
        else:
            if (pos[0] != "?listtype=__pos__"):
                pos = ["?listtype=__pos__"]
        return pos
    
    # 座標の変数をリストに戻します
    def DeletePosition(self, pos:list):
        if (pos[0] == "?listtype=__pos__"):
            pos = []
        return pos
    
    # 座標の変数であるかを出力します
    def IsPositionVar(self, pos:list):
        if (pos[0] == "?listtype=__pos__"):
            print("True")
        else:
            print("False")
    
    # 座標を追加します
    def add(self, pos:list):
        adda = [self._x, self._y]
        if (pos[0] == "?listtype=__pos__"):
            if (pos not in adda):
                pos.append(adda)
        else:
            raise TypeError("can only concatenate list (not 'position') to position")
        return pos
    
    # 座標を削除します
    def delete(self, pos:list):
        dela = [self._x, self._y]
        pos.remove(dela)
        return pos
    
    # 座標の要素を取得します
    def GetPos(self, plece:int, pos:list):
        _x = pos[plece][0]
        _y = pos[plece][1]
        return [_x, _y]

    # 座標の場所を求めます
    def FindPlece(self, pos:list):
        FindA = [self._x, self._y]
        FindB = pos.index(FindA)
        if (FindB != -1):
            return FindB
        else:
            return None
    
    # 座標をjsonファイルとして出力します
    def ExportFile(self, path:F, pos:list) -> F:
        if system.platform == "win32":
            raise PlatformError("mathworks.position.ExportFile cannot using for platform win32.")
        wait = time.sleep
        paths:F = path + ".log"
        if (os.path.exists(paths)):
            print("The file name '" + paths + "' already exists.")
            wait(0.75)
            print("Do you want to replace it?")
            print("Y:Yes, OtherButton:No")
            inputkey = input()
            if (inputkey == "Y"):
                print("Opening Files...")
                with open(paths, 'w', encoding='utf-8') as file:
                    print("Writeing...")
                    for A in range(len(pos)):
                        file.write(pos[A])
                print("Finish!")
            else:
                print("File export failed.")
        else:
            print("New files is Createing...")
            with open(paths, 'w', encoding='utf-8') as file:
                print("New files was Create.")
                wait(0.5)
                print("Writeing...")
                for A in range(len(pos)):
                    file.write(pos[A])
            print("Finish!")

# オリジナルエラー一覧:
class CodeError(Exception): ...
class PlatformError(Exception): ...
class ValueError(Exception): ...