"""
[True, True, True,.. ]  100
n*2
n*3
n*4
...
n*100
"""
size = 10
Lamp = [True for x in range(size)]


def swap(n):
    if n:
        return False
    else:
        return True


def solution():
    for i in range(2,size+1):
        for j in range(i, size+1, i):
            for k in range(2, size+1):
                if j == k:
                    Lamp[j-1] = swap(Lamp[j-1])
    return Lamp

print solution()


