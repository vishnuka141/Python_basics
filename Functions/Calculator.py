def add(n1, n2):
    result = n1 + n2
    print('result of addition :', result)


def sub(n1, n2):
    result = n1 - n2
    print('result of subtraction :', result)


def mul(n1, n2):
    result = n1 * n2
    print('result of multiplication :', result)


def div(n1, n2):
    result = n1 / n2
    print('result of division :', result)



while True:
    choice = int(input("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Stop
Select an option"""))
    if choice<5 and choice!=0:
        num1=int(input('enter 2 numbers\n'))
        num2=int(input())

        if choice==1:
            add(num1,num2)
        elif choice==2:
            sub(num1,num2)
        elif choice==3:
            mul(num1,num2)
        elif choice==4:
            div(num1,num2)
    elif choice==5:
        print('program stopped')
        break
    else:
        print('\nInvalid option')



