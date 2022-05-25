for i in range(6):
    for j in range(6-i):
        print(end=" ")
    for j in range(i):
        print('*',end=' ')
    print()

for k in range(6):
    for l in range(k):
        print(end=' ')
    for l in range(6-k):
        print('*',end=' ')
    print()