class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_str = "".join(filter(str.isalnum, s)).lower()
        print(clear_str)

        n = len(clear_str)
        first = (n // 2) - 1
        second = n // 2

        if len(clear_str) % 2 != 0:
            second += 1

        while first >= 0:
            if clear_str[first] != clear_str[second]:
                return False
            first -= 1
            second += 1

        return True


solution = Solution()
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))
# print(solution.isPalindrome("race a car"))
# print(solution.isPalindrome(" "))
# print(solution.isPalindrome("ab"))
# print(solution.isPalindrome('Marge, let\'s "[went]." I await {news} telegram.'))
print(solution.isPalindrome("0P"))
