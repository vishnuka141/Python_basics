n=5
for i in range(n):
    for j in range(n-i):
        print(end=' ')
    for k in range(i):
        print('*',end=" ")
    print()