# def pal():
#     string=input('enter a word ')
#     if string==string[::-1]:
#         print('palindrome')
#     else:
#         print('not a palindrome')
# pal()
# def pal(string):
#     if string==string[::-1]:
#         print('palindrome')
#     else:
#         print('not a palindrome')
# string=input('enter a word ')
# pal(string)

def pal(string):
    if string==string[::-1]:
        return ('palindrome')
    else:
        return ('not a palindrome')
string=input('enter a word ')
print(pal(string))

