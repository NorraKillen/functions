def comparator(num):
    k = 0
    for i in range(len(num)):
        k += int(num[i])
    return k
nums = input().split()
print(*sorted(nums, key=comparator))