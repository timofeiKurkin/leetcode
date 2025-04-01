class TrieNode {
    children: { [key in string]: TrieNode }
    isEnd: boolean

    constructor() {
        this.children = {}
        this.isEnd = false
    }
}

class WordDictionary {
    root: TrieNode

    constructor() {
        this.root = new TrieNode()
    }

    addWord(word: string): void {
        let node = this.root

        for (const letter of word) {
            if (!(letter in node.children))
                node.children[letter] = new TrieNode()
            node = node.children[letter]
        }

        node.isEnd = true
    }

    search(word: string): boolean {
        const dfs = (node: TrieNode, index: number): boolean => {
            if (index === word.length)
                return node.isEnd

            if (word[index] == ".") {
                for (const child of Object.values(node.children)) {
                    if (dfs(child, index + 1))
                        return true
                }
                return false
            }
            return word[index] in node.children && dfs(node.children[word[index]], index + 1)
        }

        return dfs(this.root, 0)
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

export { }

