# push to add element in last
# pop to delete the last element
lst=[]
count=0

size=int(input('enter the size of the stack: '))
def push():
    global count
    if count < size:
        pu = int(input('enter the element to add '))
        lst.append(pu)
        count += 1
    else:
        print('stack is full')
    print(lst)
def pop():
    global  count
    if count > 0:
        lst.pop()
        count -= 1
    else:
        print('stack is empty')
    print(lst)

while True:
    option=int(input("""1.push 
2.pop"""))
    if option==1:
        push()
    elif option==2:
        pop()
    else:
        print('exit program')
        break