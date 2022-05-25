class Mark:

    def max_mark(self):
        lst=[]
        f=open('mark.txt','r')
        for i in f:
            e=i.rstrip('\n')

            a=e.split(",")
            lst.append(a[-1])

            s=sorted(lst)
            if s[-1] in a:
                print(a)


m=Mark()
m.max_mark()

