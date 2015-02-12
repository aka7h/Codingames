import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input())
# the number of temperatures to analyse
 # the N temperatures expressed as integers ranging from -273 to 5526
r=[]
if N==0:
    print('0')
else:
    TEMP = input()
    r = [int(i) for i in TEMP.split(' ')]
    m = r[0]
    for x in r:
        if abs(x) < abs(m):
            m = x
        if abs(m) in r:
            m = abs(m)       
    print (m)
