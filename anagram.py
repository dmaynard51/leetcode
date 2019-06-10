import string

A = [100,100,40]
B = [40,40,20,30,50,60,70,40]


final = []
num = 0

for i in range (0, len(A)):
    for p in range (0, len(B)):
        if A[i] == B[p]:
            final.append(p)
            break

print final