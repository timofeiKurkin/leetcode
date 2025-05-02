from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        m, n = len(board), len(board[0])
        res: List[str] = []

        for i in range(m):
            for j in range(n):
                paths = []
                path = ""
                self.run(trie.root, i, j, path, paths, board)
                res += paths

        return res

    def run(
        self,
        root: TrieNode,
        i: int,
        j: int,
        path: str,
        paths: List[str],
        board: List[List[str]],
    ) -> None:
        if root.is_word:
            paths.append(path)
            root.is_word = False

        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] not in root.children:
            return

        letter = board[i][j]
        board[i][j] = "."
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = i + dir[0], j + dir[1]
            self.run(root.children[letter], new_i, new_j, path + letter, paths, board)
        board[i][j] = letter

        if len(root.children[letter].children) == 0:
            del root.children[letter]


solution = Solution()
print(
    solution.findWords(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
)
