class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordsEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

        curr.isWordsEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        i = 0

        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1

        return curr.isWordsEnd and i == len(word)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        i = 0

        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1

        return i == len(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
