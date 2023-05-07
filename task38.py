a, b = int(input()), int(input())
l = []
for i in range(a, b+1):
    if i % 10 != 0:
        count = 0
        for j in range(0, len(str(i))):
            if int(str(i)[j]) != 0 and i % int(str(i)[j]) == 0:
                count += 1
                if count == len(str(i)):
                    l.append(i)
            else:
                break
print(*l)