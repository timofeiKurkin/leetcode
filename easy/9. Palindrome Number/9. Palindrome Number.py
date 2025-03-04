class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_str = str(x)
        if len(num_str) == 1:
            return True

        first, second = 0, len(num_str) - 1

        while first <= len(num_str) / 2:
            if num_str[first] != num_str[second]:
                return False
            first += 1
            second += 1

        return True
