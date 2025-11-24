#32
a = {1, 2, 3, 4, 5}
b = {1, 10, 200, 4 , 30}
print(a|b, a&b) #union, intersection
## {1, 2, 3, 4, 5, 200, 10, 30} {1, 4}


#33
a = {1, 2, 3, 4, 5}
b = {1, 10, 200, 4 , 30}
print(a-b, a^b) #difference, symmetric difference
## {2, 3, 5} {2, 3, 5, 200, 10, 30}


#34
b = {1, 10, 200, 4 , 30}
b |= {100} #update method
print(b)
## {1, 4, 100, 200, 10, 30}


#35
a = {100, 200, 300, 400, 500}
a &= {400, 500, 600, 700, 800} #intersection_update method
a -= {400, 500, 600, 700, 800} #difference_update method
a ^= {400, 500, 600, 700, 800} #symmetric_difference_update method
print(a)
## {800, 400, 500, 600, 700}


#36
a = {100, 200, 300, 400, 500}
if a < {100, 200, 300, 400, 500}:
    print('부분')
elif a > {100, 200, 300, 400, 500}:
    print('상위')
else:
    print('동시')
## 동시


#37
b = {1, 10, 200, 4 , 30}
b.add(1000)
b.pop()
print(b)
## {4, 200, 1000, 10, 30}


#38
m = {x for x in range(1, 101)
        if x%3 == 0 and x%5 ==0}
print(m)
## {75, 45, 15, 90, 60, 30}