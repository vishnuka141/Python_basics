# add enqueue add in last
# remove dequeue remove first element
queue=[]
size=int(input('enter a size: '))
top=0
def enqueue():
    global top
    if top<size:
        qu = int(input('enter the element to add '))
        queue.append(qu)
        top+=1
    else:
        print('queue is full')
    print(queue)


def dequeue():
    global  top
    if top>0:
        queue.remove(queue[0])
        top-=1
    else:
        print('queue is empty')
    print(queue)
while True:
    option=int(input('enter option\n1.enqueue\n2.dequeue'))
    if option==1:
        enqueue()
    elif option==2:
        dequeue()
    else:
        print('stopped')
        break
