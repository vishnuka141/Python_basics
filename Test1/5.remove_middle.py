b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
middle=len(b)//2
b.remove(b[middle])
b.remove(b[middle-1])
print(b)