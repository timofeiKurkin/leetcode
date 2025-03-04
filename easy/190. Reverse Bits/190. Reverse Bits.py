class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:][::-1].ljust(32, "0")
        reversed_bits = int(binary, 2)
        return reversed_bits


solution = Solution()
print(solution.reverseBits(n=0b00000010100101000001111010011100))
# print(solution.reverseBits(n=0o11111111111111111111111111111101))
