from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # pq = []
        # for num in nums:
        #     heapq.heappush(pq, -num)
        # max_values: Set[int] = set()
        # for _ in range(k):
        #     max_values.add(abs(heapq.heappop(pq)))
        # if len(max_values) > 1:
        #     return 0
        # res = 0
        # max_value = max_values.pop()
        # for right in range(len(nums)):
        #     if nums[right] == max_value:
        #         res += right + 1
        # return res

        if k > len(nums):
            return 0

        # pq = []
        # for num in nums:
        #     heapq.heappush(pq, -num)
        # max_values: Set[int] = set()
        # for _ in range(k):
        #     max_values.add(abs(heapq.heappop(pq)))
        # if len(max_values) > 1:
        #     return 0

        max_value = max(nums)

        res = 0
        left = 0
        k_count = 0

        for right in range(len(nums)):
            k_count += 1 if nums[right] == max_value else 0

            while k_count >= k:
                if nums[left] == max_value:
                    k_count -= 1
                left += 1
            res += left

        return res


solution = Solution()
print(solution.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
print("")
print(solution.countSubarrays(nums=[1, 4, 2, 1], k=3))
print("")
print(
    solution.countSubarrays(
        nums=[
            61,
            23,
            38,
            23,
            56,
            40,
            82,
            56,
            82,
            82,
            82,
            70,
            8,
            69,
            8,
            7,
            19,
            14,
            58,
            42,
            82,
            10,
            82,
            78,
            15,
            82,
        ],
        k=2,
    )
)
