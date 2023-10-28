from os import path as os
import time

# 座標に関するクラスです
class Position(type):

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
    def ExportFile(self, path, pos:list):
        wait = time.sleep
        paths = path + ".log"
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
