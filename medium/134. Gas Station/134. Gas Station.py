from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)  # Gas length
        tank = 0
        curr_tank = 0
        start = 0

        for i in range(l):
            tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                curr_tank = 0
                start = i + 1

        return start if tank >= 0 else -1


solution = Solution()

print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
