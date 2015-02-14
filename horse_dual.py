import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
l=[]
N = int(input())
for i in range(N):
    Pi = int(input())
    l.append(Pi)
l.sort()
r = l[1] - l[0]
for x in range(N-1):
    p=l[x+1]-l[x]
    if r < p:
        pass
    else:
        r = p
print(r)       
