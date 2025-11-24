# 25
k = input('k = ').split()
v = list(map(int,input('v = ').split()))
result = {k[0] : v[0], k[1] : v[1], k[2] : v[2], k[3] : v[3]}

print(result)


#26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
e = park.get('english')
s = park.get('science')

print(e,s)


#27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
x = dict.fromkeys(kim, 100)
print(x)


#28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
if 'english' in lee:
    del lee['english']

print(lee)


#29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for i, j in lim.items():
    print(i,j)


#30 (90점 이상인 key 출력)
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for i,j in choi.items():
    if int(j) >= 90:
        print(j)


#31 (4과목 평균)
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
result = 0
for i,j in yoo.items():
    result += j

print(result//len(yoo))