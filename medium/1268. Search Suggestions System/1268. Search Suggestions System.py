from collections import defaultdict
from typing import List


class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = defaultdict(list)
        products.sort()

        for i in range(1, len(searchWord) + 1):
            pref = searchWord[:i]

            for product in products:
                if len(trie[pref]) == 3:
                    break

                if product.startswith(pref):
                    trie[pref].append(product)

        return [x for x in trie.values()]


solution = Solution()
print(
    solution.suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse",
    )
)
