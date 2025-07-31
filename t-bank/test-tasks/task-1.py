# A - Payment for subscription


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

a, b, c, d = map(int, input().split(" "))

total = a
traffic = b - d

if traffic < 0:
    total += abs(traffic) * c

print(total)
