t = int(input())

for _ in range(t):
    n = int(input())  # array size
    nums = list(map(int, input().split(" ")))
    nums.sort()

    valid = True

    for i in range(n):
        if nums[i] > i + 1:
            valid = False
            break

    if not valid:
        print("Second")
    else:
        total = sum(nums)
        max_total = n * (n + 1) // 2
        T = max_total - total
        if T % 2 == 1:
            print("First")
        else:
            print("Second")
