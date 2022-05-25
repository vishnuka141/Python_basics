score = int(input('enter the mark: '))
if score > 100:
    print('Invalid score')
elif score >= 90:
    print('A+ ')
elif score >= 80:
    print('A')
elif score >= 70:
    print('B+')
elif score >= 60:
    print('B')
elif score >= 50:
    print('C+')
elif score < 50:
    print("Failed")
