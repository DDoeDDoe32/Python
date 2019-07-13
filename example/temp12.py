'''
f = open('C:/workspace/Python/example/textFile.txt', 'a')
f.write('\nHello python')
f.close()
'''

'''
f = open('C:/workspace/Python/example/textFile.txt', 'r')
print('f.read() : {0}'.format(f.read()))
f.close()
'''

'''
ts = ['hello python\n', 'hello c++\n', 'hello java\n']

with open('C:/workspace/Python/example/textFile.txt', 'w') as f :
'''
'''
for tl in ts :
    f.write(tl)
    f.writelines(ts)

'''
'''
with open('C:/workspace/Python/example/textFile.txt', 'r') as f :
    ls = f.readlines()
    print('type(ls) : {0}'.format(type(ls)))

    l = ''
    for l in ls :
        print(l, end='')
'''
with open('C:/workspace/Python/example/textFile.txt', 'r') as f :
    l = f.readline()
    print('type(ls) : {0}'.format(type(l)))

    c = 1

    while l != '' :
        print(l, end='')
        l = f.readline()
        c += 1

    print('c-1 : {0}'.format(c-1))
        
