from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # candies = len(ratings)
        # i = 1

        # if ratings[0] > ratings[i]:
        #     candies[0] = 2

        # while i < len(ratings) - 1:
        #     curr = ratings[i]
        #     next_child = ratings[i + 1]
        #     prev_child = ratings[i - 1]

        #     if curr >= next_child and curr >= prev_child:
        #         candies[i] = candies[i - 1] + candies[i + 1]

        #     i += 1

        # if ratings[-1] > ratings[-2]:
        #     candies[-1] = candies[-2] + 1

        # return sum(candies)

        n = len(ratings)
        candies = [1] * len(ratings)

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


solution = Solution()

print(solution.candy([1, 0, 2]))
print(solution.candy([1, 2, 2]))
print(solution.candy([1, 2, 87, 87, 87, 2, 1]))  # 7 + 5 + 1(?) = 13
