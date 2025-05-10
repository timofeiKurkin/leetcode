from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        items = defaultdict(int)

        for num in arr:
            items[num] += 1

        occurs = set()
        for _, o in items.items():
            if o in occurs:
                return False
            occurs.add(o)

        return True
