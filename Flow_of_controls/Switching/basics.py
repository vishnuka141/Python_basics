#switching
# break
# continue

# for i in range(5):
#     print(i)
#     if i==3:
#         break

for i in range(4):
    for j in range(5):
        if j==2:
            print(j)
            break
        print(j)
    print('inside i ',i)

