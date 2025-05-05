class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        j = 0

        for i in range(len(word1)):
            if j < len(word2):
                res += word1[i] + word2[j]
                j += 1
            else:
                res += word1[i:]
                break

        if j != len(word2) - 1:
            res += word2[j - 1 :]

        return res


print(
    "PmsptAoauFfFCxkNbvPZYpCMHfotMrFAadMXxNxECzToVmmNSYjFCjetSUTZKapKVHfmfgKYAdMpRAUArHhGksVvDtGzYOwYZgZJ".lower()
)
print(
    "ObnHTYfOxcwxDTRdUDuFFfjXcqfGFYnPorpGzXCYrXAEeenxJYfSvhZrakmzubZexNerqnvXaVqvjKXSxHPzYFRBJUFmhUSPMDtn".lower()
)
