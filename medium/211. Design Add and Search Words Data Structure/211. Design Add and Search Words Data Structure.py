from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWordsEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        structure = self.root

        for letter in word:
            if letter not in structure.children:
                structure.children[letter] = TrieNode()
            structure = structure.children[letter]

        structure.isWordsEnd = True

    def search(self, word: str) -> bool:
        def dfs(structure: TrieNode, index: int) -> bool:
            if index == len(word):
                return structure.isWordsEnd

            if word[index] == ".":
                for child in structure.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                return word[index] in structure.children and dfs(
                    structure.children[word[index]], index + 1
                )

        return dfs(self.root, 0)


solution = WordDictionary()
solution.addWord("bad")
solution.addWord("dad")
solution.addWord("mad")
print(solution.search("pad"))
print(solution.search("bad"))
print(solution.search(".ad"))
print(solution.search("b.."))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
