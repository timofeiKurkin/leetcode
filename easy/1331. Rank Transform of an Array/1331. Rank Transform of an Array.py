from typing import Dict, List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        res: Dict = {}
        rank = 1

        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in res:
                res[sorted_arr[i]] = rank
                rank += 1

        return [res[item] for item in arr]


solution = Solution()
print(solution.arrayRankTransform([40, 10, 20, 30]))
print(solution.arrayRankTransform([100, 100, 100]))
print(solution.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
