m = int(input(" m : base  and number of alphabets"))
n = int(input(" n : empty spaces / combination"))

def prxnt(L):
    for i in range(len(L)):
        print(L[i])
        
base = []
temp = []
for i in range(m ** n):
    x = i
    if (x < m):
        temp.insert(0, x)
        base.append(temp) 
        temp = [] 
        continue # skip everything down there    
    while x > 0:
        remainder = x % m
        temp.insert(0, remainder)
        x = (x // m)
        
    base.append(temp)
    temp = []
    
for i in range(len(base)):
    while len(base[i]) < n:
        base[i].insert(0,0)
        
alph = ['A','B','C','D','E']
tmep = []

##for i in range(len(base)):
##    for j in range(len(base[i])):
##        base[i][j] = alph[base[i][j]]
prxnt(base)

tmpe = []
adList = []
falseTable = []
termp = [] 
for i in range(len(base)):
    tmpe.insert(0,i)
    termp.insert(0,i)
    for j in range(len(base)):
        if base[i][0 - (n - 1):] == base[j][:(n - 1)] and i != j:
            tmpe.append(j)
            termp.append(False)
    adList.append(tmpe)
    falseTable.append(termp)
    tmpe = []
    termp = []

prxnt(adList)
prxnt(falseTable)

cango = []
possibleways = [] 
startpos = falseTable[0][0]
nextpos = startpos
megastop = False

while megastop == False:
    cango = []
    while True:
        position = nextpos
        cango.append(position)
        if position == startpos and len(cango) > 1:
            break 
        x = 1 
        while falseTable[position][x] == True:
            x = x + 1
        nextpos = adList[position][x]
        falseTable[position][x] = True
    possibleways.append(cango)
        
    found = False 
    for i in range(len(adList)):
        y = i
        for j in range(1,len(falseTable[y])):
            if falseTable[y][j] == False:
                nextpos = y
                found = True 
                break     
        if found == True :
            break
    if i == len(adList)-1 and found == False:
        megastop = True         
    startpos = nextpos 

finalpath = []
print(possibleways)
for i in range(len(possibleways[0])):
    finalpath.append(possibleways[0][i])
    print(finalpath)
del possibleways[0]

while len(possibleways) != 0:
    leftside = []
    rightside = []
    firstItem = possibleways[0][0]
    for j in range(len(finalpath)):
        if firstItem == finalpath[j]:
            leftside = finalpath[:j+1]
            rightside = finalpath[j+1:]
            break    
    del possibleways[0][0]
    
    finalpath = [] 
    for i in range(len(leftside)):
        finalpath.append(leftside[i])
    for i in range(len(possibleways[0])):
        finalpath.append(possibleways[0][i])
    for i in range(len(rightside)):
        finalpath.append(rightside[i])
        
    del possibleways[0]    
print(finalpath)

for i in range(len(finalpath)):
##    for j in range(len(base)):
##        finalpath[i] = finalpath[base[i]]
    finalpath[i] = base[i]
##        break 

        
