'''
list = ['a', 'hello', 123, 3.14]

for i in list :
    print(i)

print('end')

tuple = ('A', 'HELLO', 456, 0.333) # 수정 불가능
for i in tuple :
    print(i)

dic = {'홍길동': 20, '홍길자': 30, '홍길순': 40}
for i in dic :
    print(i) # 키값 출력
    print(dic[i])

    print('{0}의 나이 : {1}'.format(i, dic[i]))
'''
""" 
# 구구단
for i in range(2, 10, 1) : 
    for y in range(1, 10, 1) :
        print('{0} * {1} = {2}'.format(i, y, (i*y)))

"""
'''
count = 0
target = 100
sum = 0
while count <= target:
    sum = sum + count
    count = count + 1

print('0부터 {0} 까지의 합 : {1}'.format(target,sum))

'''

for i in range(10) :
    if((i%2) == 0) :
        continue
    print(i)

for i in range(10) :
    if( i > 5) :
        break
    print(i)
