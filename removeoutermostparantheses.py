
S = "(()())(())"
        
res, opened = [], 0
final = ""

for c in S:
    if c == '(' and opened > 0: 
        final += c
    if c == ')' and opened > 1: 
        final += c
    if c == '(':
        opened += 1
    else:
        opened -= 1
        
print final