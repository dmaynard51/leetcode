
A = [5,1,5,2,5,3,5,4]
uniqueNumber = (len(A)/2) + 1
duplicate = len(A) / 2
iterator = 0

uniqueSet = set()
uniqueList = []
uniqueFinal = []

for x in A:
    if x not in uniqueSet:
        uniqueSet.add(x)
        uniqueList.append(x)

for x in uniqueList:
    iterator = 0
    for y in A:
        if y == x:
            iterator +=1
        if iterator == duplicate:
            uniqueFinal.append(x)
print uniqueFinal[0]
