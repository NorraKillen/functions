import string
b = input()
a = all([any(map(lambda x: x.isdigit(), b)), any(map(lambda x : x.islower(), b)), any(map(lambda x : x.isupper(), b)), len(b) >= 7])
if a == True:
    print('YES')
else:
    print('NO')