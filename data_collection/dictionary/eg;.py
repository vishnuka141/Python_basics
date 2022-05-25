d={'name':'vishnu','age':33}
d['place']='kochi'
d['age']=34##key is not added value is changing
d.update({'school':'ko'})

del d['age']#to remove the element
d.clear()
del d
print(d)