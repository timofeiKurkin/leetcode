class Solution:
    def countLargestGroup(self, n: int) -> int:
        nums = {}
        max_size = 0
        res = 0

        for num in range(1, n + 1):
            d_sum = sum(map(int, str(num)))

            if d_sum in nums:
                nums[d_sum].append(num)
            else:
                nums[d_sum] = [num]

            s = len(nums[d_sum])

            if s == max_size:
                res += 1
            elif s > max_size:
                res = 0
                max_size = s

        return res + 1
