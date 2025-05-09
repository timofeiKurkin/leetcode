from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0] * (len(gain) + 1)

        for i in range(len(gain)):
            altitudes[i + 1] = altitudes[i] + gain[i]

        return max(altitudes)
