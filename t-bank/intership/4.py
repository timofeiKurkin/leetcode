#  3
# 0 10 5
# 0 10 2
# 0 0 1

# a = [5] [2] [1]


# n = int(input())  # 1 <= n <= 6 * 10^5
# l = [0] * n
# r = [0] * n
# a = [0] * n

# for i in range(n):
#     # l - max water flow from i to i - 1 before clogging
#     # r - max water flow from i to i + 1 before clogging
#     # a - capacity of i reservoir
#     li, ri, ai = map(int, input().split())
#     l[i] = li
#     r[i] = ri
#     a[i] = ai

# prefix_sum = [0] * (n + 1)
# for i in range(n):
#     prefix_sum[i + 1] = prefix_sum[i] + a[i]

# # water from left to right
# right_flow = [0] * n
# j = 0
# flow = 0
# for i in range(n):
#     if i > j:
#         j = i
#         flow = 0
#     while j < n - 1 and flow + r[j] >= a[j + 1]:
#         flow += r[j]
#         j += 1
#         flow -= a[j]
#         flow = max(flow, 0)
#     right_flow[i] = j

# # water from right to left
# left_flow = [0] * n
# j = n - 1
# flow = 0
# for i in range(n - 1, -1, -1):
#     if i < j:
#         j = i
#         flow = 0
#     while j > 0 and flow + l[j] >= a[j - 1]:
#         flow += l[j]
#         j -= 1
#         flow -= a[j]
#         flow = max(flow, 0)
#     left_flow[i] = j

# max_water = 0
# for i in range(n):
#     total = prefix_sum[right_flow[i] + 1] - prefix_sum[left_flow[i]]
#     max_water = max(max_water, total)

# print(max_water)

n = int(input())
l = [0] * (n + 1)
r = [0] * (n + 1)
a = [0] * (n + 1)

for i in range(1, n + 1):
    # l - max water flow from i to i - 1 before clogging
    # r - max water flow from i to i + 1 before clogging
    # a - capacity of i reservoir
    li, ri, ai = map(int, input().split())
    l[i] = li
    r[i] = ri
    a[i] = ai

left_flow = [0] * (n + 1)
if n >= 1:
    threshold_prev = a[1]
    value_prev = a[1]
    for i in range(2, n + 1):
        if l[i] <= threshold_prev:
            left_flow[i] = l[i]
            threshold_curr = a[i] + l[i]
            value_curr = a[i] + l[i]
        else:
            left_flow[i] = value_prev
            threshold_curr = a[i] + threshold_prev
            value_curr = a[i] + value_prev
        threshold_prev = threshold_curr
        value_prev = value_curr

right_flow = [0] * (n + 1)
if n >= 1:
    threshold_next = a[n]
    value_next = a[n]
    for i in range(n - 1, 0, -1):
        if r[i] <= threshold_next:
            right_flow[i] = r[i]
            threshold_curr = a[i] + r[i]
            value_curr = a[i] + r[i]
        else:
            right_flow[i] = value_next
            threshold_curr = a[i] + threshold_next
            value_curr = a[i] + value_next
        threshold_next = threshold_curr
        value_next = value_curr

ans = 0
for i in range(1, n + 1):
    total = a[i] + left_flow[i] + right_flow[i]
    if total > ans:
        ans = total

print(ans)
