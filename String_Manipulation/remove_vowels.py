str=input('enter a string ')
vowel= 'aeiou'
new= " "
for i in str:
    if i not in vowel:
        new=new+i

print(new)
