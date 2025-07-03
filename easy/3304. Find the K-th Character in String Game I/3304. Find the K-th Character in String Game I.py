class Solution:
    def kthCharacter(self, k: int) -> str:
        return self.solution1(k)

    def solution1(self, k: int) -> str:
        word = "ab"
        generated = "b"

        while len(word) <= k:

            new_part: str = ""
            for i in range(len(generated)):
                new_part += chr(ord("a") + (ord(generated[i]) - ord("a") + 1) % 26)

            generated += new_part
            word += generated

        return word[k - 1]

    def solution2(self, k: int) -> str:
        word = "a"

        while len(word) <= k:

            new_part: str = ""
            for i in range(len(word)):
                new_part += chr(ord("a") + (ord(word[i]) - ord("a") + 1) % 26)

            word += new_part

        return word[k - 1]


solution = Solution()
print(solution.kthCharacter(5))
print(solution.kthCharacter(10))
