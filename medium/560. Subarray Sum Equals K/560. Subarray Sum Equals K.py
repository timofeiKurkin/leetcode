from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ht = defaultdict(int)
        ht[0] = 1

        total = 0
        res = 0

        for num in nums:
            total += num
            sub_array = total - k
            
            res += ht[sub_array]
            ht[total] = 1 + ht[total]

        return res
