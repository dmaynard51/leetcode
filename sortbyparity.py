
A = [3,1,2,4]
even = []
odd = []
final = []

for x in A:
    if x % 2 != 0:
        odd.append(x)
    else:
        even.append(x)

final += even
final += odd

print final
