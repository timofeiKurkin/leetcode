# 1 <= N <= 2 * 10^9

# Binary tree
parts = int(input())
queue = [parts]
res = 0
while queue:
    for _ in range(len(queue)):
        part = queue.pop()
        part //= 2
        if part:
            queue.append(part)
    res += 1
print(res)


# n = int(input())
# k = 0
# curr = 1
# while curr < n:
#     curr *= 2
#     k += 1
# print(k)
