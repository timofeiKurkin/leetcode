class TrieNode {
    children: { [key in string]: TrieNode }
    isEnd: boolean

    constructor() {
        this.children = {}
        this.isEnd = false
    }
}

class Trie {
    root: TrieNode

    constructor() {
        this.root = new TrieNode()
    }

    insert(word: string): void {
        let current = this.root

        for (const letter of word) {
            if (!(letter in current.children))
                current.children[letter] = new TrieNode()

            current = current.children[letter]
        }

        current.isEnd = true
    }

    search(word: string): boolean {
        let current = this.root
        let i = 0

        while (i < word.length && word[i] in current.children) {
            current = current.children[word[i]]
            i += 1
        }

        return word.length === i && current.isEnd
    }

    startsWith(prefix: string): boolean {
        let current = this.root
        let i = 0

        while (i < prefix.length && prefix[i] in current.children) {
            current = current.children[prefix[i]]
            i += 1
        }

        return prefix.length === i
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */