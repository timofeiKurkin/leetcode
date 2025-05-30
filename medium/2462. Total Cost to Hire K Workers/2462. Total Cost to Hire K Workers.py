import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # res = 0
        # inf = 10 * 10
        # # heapq.heapify(costs)

        # for _ in range(k):
        #     n = len(costs)

        #     if n < candidates:
        #         res += min(costs)
        #         break

        #     left = 0
        #     # [index, cost]
        #     session_cost = [0, inf]

        #     while left < candidates:
        #         if costs[left] < session_cost[1]:
        #             session_cost = [left, costs[left]]

        #         if costs[n - left - 1] < session_cost[1]:
        #             session_cost = [n - 1 - left, costs[n - left - 1]]

        #         left += 1

        #     costs.pop(session_cost[0])
        #     res += session_cost[1]

        # return res

        n = len(costs)
        res = 0

        left = 0
        right = n - 1

        # [(index, cost), ...]
        left_hp = []
        right_hp = []

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_hp, costs[left])
                left += 1
            if left <= right:
                heapq.heappush(right_hp, costs[right])
                right -= 1

        for _ in range(k):
            if not right_hp or (left_hp and left_hp[0] <= right_hp[0]):
                cost: int = heapq.heappop(left_hp)
                if left <= right:
                    heapq.heappush(left_hp, costs[left])
                    left += 1
            else:
                cost: int = heapq.heappop(right_hp)
                if left <= right:
                    heapq.heappush(right_hp, costs[right])
                    right -= 1

            res += cost

        return res


solution = Solution()
print(solution.totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
print(solution.totalCost(costs=[1, 2, 4, 1], k=3, candidates=3))
print(
    solution.totalCost(
        costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
        k=11,
        candidates=2,
    )
)


# [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
# [31,25,72,79,74,65,84,91,18,59,27,9,81,33,58]
# [31,72,79,74,65,84,91,18,59,27,9,81,33,58]
# [72,79,74,65,84,91,18,59,27,9,81,33,58]
# [72,79,74,65,84,91,18,59,27,9,81,58]
# [79,74,65,84,91,18,59,27,9,81,58]
# [79,74,65,84,91,18,59,27,9,81]
# [79,74,65,84,91,18,59,27,81]
# [79,74,65,84,91,18,59,81]
# [79,74,65,84,91,18,81]
# [79,74,65,84,91,81]
# [79,65,84,91,81]
