str=input('enter a string ')
new=" "
r=' '
for i in str:
    if i not  in new:
        new=new+i
    else:
        r=r+i
print(r)
print(new)