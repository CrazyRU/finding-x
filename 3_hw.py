print('this code helps you to find x in this equality')
print('\nchoose 1 or 2: \n1)ax + b = 0 \n2)ax - b = 0')
f = input()
if f == '1':
    print('enter a')
    a = int(input())
    print('enter non-negative b')
    b = abs(int(input()))
    if abs(a) > 1000 or abs(b) > 1000:
        print("error, absolute numbers can't be more than 1000")
    elif a == 1:
        print('-------')
        print(0 - b)
    elif a == 0:
        print('-------')
        print('NO')
    else:
        print('-------')
        print((0 - b) / a)
elif f == '2':
    print('enter a')
    a = int(input())
    print('enter non-negative b')
    b = abs(int(input()))
    if abs(a) > 1000 or abs(b) > 1000:
        print("error, absolute numbers can't be more than 1000")
    elif a == 1:
        print('-------')
        print(0 + b)
    elif a == 0:
        print('-------')
        print('NO')
    else:
        print('-------')
        print((0 + b) / a)
else:
    print('enter 1 or 2')
    
