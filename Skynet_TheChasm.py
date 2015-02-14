import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(input()) # the length of the road before the gap.
G = int(input()) # the length of the gap.
L = int(input()) # the length of the landing platform.

# game loop
while 1:
    S = int(input()) # the motorbike's speed.
    X = int(input()) # the position on the road of the motorbike.
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if X == (R-1):
       print('JUMP')
    elif X > (R-1) :
        print('SLOW')
    elif S == (G+1):
        print('WAIT')
    elif S > (G+1):
        print('SLOW')
    else:
        print('SPEED')
