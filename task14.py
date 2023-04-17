def comparator(num):
    k = 0
    for i in range(len(str(num))):
        k += int(str(num)[i])
    return k
nums = map(int, input().split())
nums = sorted(nums)

print(*sorted(nums, key=comparator))