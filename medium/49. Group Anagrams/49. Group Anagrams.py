from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagrams: Dict[str, List[str]] = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        return [item[1] for item in anagrams.items()]


solution = Solution()

print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
