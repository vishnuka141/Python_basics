n1=5
n2=0
try:
    print(n1/n2)
except Exception as e:
    print('error',e)
finally:
    print('finished')
