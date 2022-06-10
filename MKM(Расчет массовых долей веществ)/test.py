file = open('таблица.txt').readlines()
Table = {}
for i in range(len(file)):
    Table[file[i].split()[0]] = int(file[i].split()[-1])
sub = str(input()) + '  '

BrOpen = []
BrClosed = []
i = 0
for i in range(len(sub)):
    if sub[i] == '(':
        BrOpen.append(i)
    elif sub[i] == ')':
        BrClosed.append(i)
        
if not (len(BrOpen) == len(BrClosed) and BrOpen <= BrClosed):
    print('Ошибка! Несогласованные скобки')
    exit()

#BrClosed = BrClosed[::-1]
BrOpen = BrOpen[::-1]

print(BrOpen, BrClosed)

Elements = {}
i = 0
BrMulti = 1
BrInd = 0
Multi = 0

def num(s):
    multi = ''
    i = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            multi += s[i]
        else:
            break
    if multi == '':
        return 1
    else:
        return int(multi)
    
while i <= len(sub) - 2:
    if i in BrOpen:
        print('(')
        BrMulti = num(sub[BrClosed[BrInd] + 1 : -1])
        BrInd += 1
    elif i in BrClosed:
        print(')')
        BrMulti = 1

    print(BrMulti)
        
    if sub[i:i + 2].isalpha() and sub[i + 1].islower():
        
        if not sub[i:i + 2] in Elements:
            Elements[sub[i:i + 2]] = 0
  
        if sub[i + 2].isnumeric():
            Elements[sub[i:i + 2]] += num(sub[i + 2 : -1]) * BrMulti 
        else:
            Elements[sub[i:i + 2]] += BrMulti
        
    elif sub[i].isupper() and any("()"):
        if not sub[i] in Elements:
            Elements[sub[i]] = 0
        if sub[i + 1].isnumeric():
            Elements[sub[i]] += num(sub[i + 1 : -1]) * BrMulti
        else:
            Elements[sub[i]] += BrMulti
    i += 1

print(Elements)
    
