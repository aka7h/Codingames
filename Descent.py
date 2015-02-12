import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    l=[]
    SX, SY = [int(i) for i in input().split()]
    for i in range(8):
        MH = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        l.append(MH)
        m = max(l)
        C = l.index(m)
    if SX == C:
        print('FIRE')
    else:
        print('HOLD')
