def fibonacci(n):
    # 0 1 1 2 3 5 8...
    # if n=4 nth term(4th term)=2
    # n-1th term 1, n-2th term 1
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(10):
    print(fibonacci(i),end=' ')