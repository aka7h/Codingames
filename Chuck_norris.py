MESSAGE = input()
bit,out='',''
def tex(i,j):
    global out
    if int(j) == 1:
        out+='0 '+('0'*i)+' '
    else:
        out+='00 '+('0'*i)+' '
    return out
    
Text = [x for x in MESSAGE]
for x in Text:
    Char_binary = bin(ord(x))[2:]
    if len(Char_binary) == 6:
        Char_binary = '0'+Char_binary
    bit+=Char_binary

count=0
temp = Char_binary[0]

for x in bit:
    if x == temp:
        count+=1
    else:
        tex(count,temp)
        temp = x
        count=1
tex(count,temp)
print(out.rstrip())
