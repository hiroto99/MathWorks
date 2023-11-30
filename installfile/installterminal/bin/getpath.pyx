import os

cdef getpath():
    path = os.path.abspath('mathworks')
    return path

def main():
    a = getpath()
    return a