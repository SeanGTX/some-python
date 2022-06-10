file = open('таблица.txt').readlines()
Table = {}
for i in range(len(file)):
    Table[file[i].split()[0]] = int(file[i].split()[-1])
sub = str(input()) + ' '
if sub == ' ':
    print('Ошибка! пустой ввод')
    exit()
elif '0' in sub:
    print('Ошибка! В формуле содержится 0')
    exit()
DivStr = []
i = 0
err = False
errSym = ''
while i <= len(sub) - 1:
    if (sub[i].isupper() and sub[i + 1].islower()) or (sub[i].isnumeric() and sub[i + 1].isnumeric()):
        if (not sub[i:i + 2] in Table) and not (sub[i].isnumeric() and sub[i + 1].isnumeric()):
            err = True
            errSym = sub[i:i + 2] 
            break
        DivStr.append(sub[i:i + 2])
        i += 1
        
    elif not sub[i].islower():
        if (not sub[i] in Table) and not (sub[i] == '(' or sub[i] == ')' or sub[i] == ' ') and not sub[i].isnumeric() :
            err = True
            errSym = sub[i]
            break
        DivStr.append(sub[i])
    i += 1
if err:
    print('Ошибка! Неверный знак в формуле ' + errSym)
    exit()
    
i = 0 
BrIndex = []
for i in range(len(DivStr)):
    if '(' == DivStr[i] == ')':
        BrIndex.append(i)
i = 0
if len(BrIndex) != 0:
    for i in range(len(BrIndex)):
        print(i)

print(BrIndex)

i = 0
m = 0
Brackets = 0
CheckBrackets = False
if len(DivStr) != 1:
    while DivStr[i] != ' ':
        if DivStr[i] == '(' or DivStr[i] == ')':
            if DivStr[i] == '(':    
                CheckBrackets = True
            if DivStr[i] == ')':
                CheckBrackets = False
                if DivStr[i + 1].isnumeric(): 
                    m += Brackets * int(DivStr[i + 1])
                else:
                    m += Brackets
                Brackets = 0
            i += 1
            continue
        if not DivStr[i].isalpha():
             i += 1
             continue
        if CheckBrackets:
            if DivStr[i + 1].isnumeric() and '(' != DivStr[i + 1] != ')' and DivStr[i + 1] != ' ':
                Brackets += Table[DivStr[i]] * int(DivStr[i + 1])
            else:
                Brackets += Table[DivStr[i]]
        else:
            if DivStr[i + 1].isnumeric() and '(' != DivStr[i + 1] != ')' and DivStr[i + 1] != ' ':    
                m += Table[DivStr[i]] * int(DivStr[i + 1])
            else:
                m += Table[DivStr[i]]
        i += 1
    Elements = {}
    i = 0
    while i <= len(DivStr) - 1:
        if not DivStr[i] in Elements and not DivStr[i].isnumeric() and DivStr[i] != ' ' and '(' != DivStr[i] != ')':
            if DivStr[i + 1].isnumeric():
                Elements[DivStr[i]] = 0
                Elements[DivStr[i]] += int(DivStr[i + 1]) 
            else:
                Elements[DivStr[i]] = 1
        elif DivStr[i] in Elements and not DivStr[i].isnumeric() and DivStr[i] != ' ' and '(' != DivStr[i] != ')':
            if DivStr[i + 1].isnumeric():
                Elements[DivStr[i]] += int(DivStr[i + 1]) 
            else:
                Elements[DivStr[i]] += 1
        i += 1
    if '(' in DivStr:
        for i in range(DivStr.index('('), DivStr.index(')')):
            if not DivStr[i].isnumeric() and DivStr[DivStr.index(')') + 1].isnumeric() and '(' != DivStr[i] != ')':
                Elements[DivStr[i]] *= int(DivStr[DivStr.index(')') + 1])
    Elmlist = list(Elements.keys())

print('Молярная масса =', m)
if len(DivStr) > 3:
    print('Массовые доли элементов ' + sub + '(%)')
    i = 0
    for i in range(len(Elmlist)):
        print(Elmlist[i], '=', round((Table[Elmlist[i]] * Elements[Elmlist[i]] / m) * 100, 3), '%')
