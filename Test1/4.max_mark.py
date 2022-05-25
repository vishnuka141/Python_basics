Students =[('anu',97),('amal',99),('arun',65)]
lst=[]
for i in Students:
    lst.append(i[1])
lst1=(max(lst))
for i in Students:
    if i[1]==lst1:
        print(i)
