number = list(map(int, list(input())))
number.sort()

i = 0
while number[i] == 0:
    i += 1

start = number[0]
end = number[i]
number[0] = end
number[i] = start

print(int("".join(map(str, number))))
