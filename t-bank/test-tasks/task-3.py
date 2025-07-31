# 2 <= n, t <= 100
n, t = map(int, input().split(" "))
floors = list(map(int, input().split(" ")))

# 2 <= outgoing_employee <= n
leaving_employee = int(input())
leaving_employee_floor = floors[leaving_employee - 1]

min_floor, max_floor = min(floors), max(floors)

res = max_floor - min_floor
min_distance_to_leaving = min(
    abs(leaving_employee_floor - min_floor), abs(leaving_employee_floor - max_floor)
)

if min_distance_to_leaving > t:
    # if leaving_employee_floor - min_floor < max_floor - leaving_employee_floor:
    #     res = leaving_employee_floor - min_floor + max_floor - 1
    # else:
    #     res = max_floor - leaving_employee_floor + max_floor - 1
    res += min(leaving_employee_floor - min_floor, max_floor - leaving_employee_floor)

print(res)
