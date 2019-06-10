"""
:type words: List[str]
:rtype: int
"""
words = ["gin", "zen", "gig", "msg"]

for x in range(97,123):
    letter = chr(x)
    alphabet = "" + letter

morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

dictionary = {}
iterator = 0



for x in range (97, 123): 
    letter = chr(x)
    dictionary[letter] = morseCode[iterator]
    iterator += 1

final = []

#convert
iterator = 0
for x in words:
    word = ""
    #append each character to the word
    for y in x:
        word += dictionary[y]
    #if word is not in final then append
    if  word not in final:
        final.append(word)
    # reset the word
    word = ""
    
print len(final)