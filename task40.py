n = int(input())
l = all([any(map(lambda x: x == '5', [input()[-1] for j in range(int(input()))])) for i in range(n)])
if l == True:
    print( 'YES')
else:
    print('NO')