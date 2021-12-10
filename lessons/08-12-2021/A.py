n = int(input())
nums = [int(k) for k in input().split()]
k = int(input())

counter = 0
for num in nums:
    if num == k:
        counter += 1

print(counter)