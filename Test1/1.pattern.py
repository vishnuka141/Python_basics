ini_range=1
f_range=5
# for i in range(ini_range,f_range+1):
#     for j in range(i):
#         print(1,end=' ')
#     print()
# for k in range(ini_range-1,f_range):
#     for l in range(f_range-k):
#         print(2,end=' ')
#     print()
# for i in range(ini_range,f_range+1):
#     for j in range(i):
#         print(3,end=' ')
#     print()
# for k in range(ini_range-1,f_range):
#     for l in range(f_range-k):
#         print(4,end=' ')
#     print()
for i in range(ini_range,f_range):
    if i%2==1:
        for a in range(1,f_range+1):
            for j in range(a):
                print(i,end=' ')
            print()
    else:

        for a in range(f_range):
            for j in range(f_range-a):
                print(i,end=' ')
            print()