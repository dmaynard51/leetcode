A = [[1,1,0],[1,0,1],[0,0,0]]

#first reverse
for x in range(0, len(A)):
    for y in range(0, len(A[x])):
        if A[x][y] == 1:
            A[x][y] = 0
        else:
            A[x][y] = 1



#invert numbers
for x in range(0, len(A)):
    A[x] = A[x][::-1]
    #A[x].reverse()

    
print A

