from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # ht = defaultdict(bool)

        # for k, v in cnt.items():
        #     ht[k] = bool(v)

        # left, right = 0, 0
        # res = []

        # while left < len(s):
        #     while right < len(s) and ht[s[right]]:
        #         cnt[s[right]] -= 1
        #         ht[s[right]] = bool(cnt[s[right]])
        #         right += 1

        #     res.append(right - left)
        #     left = right

        # return res

        ht = {}

        for i, sym in enumerate(s):
            ht[sym] = i

        start, end = 0, 0
        res = []

        for i, sym in enumerate(s):
            end = max(end, ht[sym])

            if i == end:
                res.append((end - start) + 1)
                start = i + 1

        return res


solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij"))
print(solution.partitionLabels("eccbbbbdec"))
