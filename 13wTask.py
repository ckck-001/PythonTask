#39
a = int(input('양수 입력'))
def function39(a):
    for i in range(0, a+1):
        if i %2!=0:
            print(i)

function39(a)

#40
b = int(input('숫자 입력'))
def function40(b):
    if b % 3 ==0:
        print(b)

function40(b)

#41
c0, c1, c2, c3 = map(int,input('숫자 4개 입력').split())
def function41(a, b, c, d):
    l = (a,b,c,d)
    print(max(l), min(l))

function41(c0, c1, c2, c3)

#42 #39와 동일

#43
d = int(input('0보다 크거나 같은 정수 n 입력'))
def function43(d):
    if d == 0:
        print(0)
    else:
        result = 1
        for i in range(d, 1, -1):
            print(i,'* ',end='')
            result*=i
        print('1 =', result)

function43(d)

#44
e0, e1= map(int,input('2이상 9이하의 양수 2개 입력').split())
def function44(a, b):
    result = 0
    for i in range(a, b+1):
        for j in range(a, b+1):
            if i*j >= 30:
                print(i, ' * ', j)
                result += 1
    print(result)
function44(e0, e1)

#45
a = [1, 2, 3, 4, 5]
def function45(a):
    result = 0
    for i in a:
        result += i
    print(result)
function45(a)
