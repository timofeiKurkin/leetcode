class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda symbol: symbol, s.split(" ")))[-1])
