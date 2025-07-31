# 1 <= n <= 1000 | 1 <= k <= 10^4
n, k = map(int, input().split(" "))

# 1 <= len(numbers) <= n
# 1 <= numbers[i] <= 10^9
numbers = input().split(" ")

bargains = []

for num in numbers:
    capacity = len(num)
    for i, num in enumerate(num):
        if num == "9":
            continue

        bargains.append(10 ** (capacity - i - 1) * (9 - int(num)))


bargains.sort(reverse=True)
print(sum(bargains[:k]))

# def calculate_bargain(x: int, total: int) -> int:
#     n_x = len(str(x)) - 1
#     new_total = total
#     remind_k = k
#     for i, s in enumerate(str(x)):
#         if not remind_k:
#             break
#         if s == "9":
#             continue
#         m_local = pow(10, n_x - i)
#         new_total -= int(s) * m_local
#         new_total += 9 * m_local
#     print(f"{new_total=}", f"{total=}")
#     return new_total

# numbers.sort(key=lambda x: calculate_bargain(x, start_sum), reverse=True)
