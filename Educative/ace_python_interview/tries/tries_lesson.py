from collections import deque


class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word is None:
            return None
        curr = self.root

        for char in word:
            # if not exist, create a node
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            # if exists, move to that node
            curr = curr.children[char]

        curr.endOfWord = True

        return None

    def search(self, word: str) -> bool:
        if word is None:
            return False

        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # if exists, check it is denoted as end of word
        return curr.endOfWord

    def startsWith(self, word: str) -> bool:
        if word is None:
            return False

        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

    def countWords(self):
        if not self.root:
            return 0

        q = deque([self.root])
        wordsCount = 0
        while q:
            curr = q.popleft()

            if curr.children:
                for value in curr.children.values():
                    if value.endOfWord == True:
                        wordsCount += 1
                    q.append(value)
        return wordsCount


Words = Trie()

Words.insert("apple")
Words.insert("carpet")
Words.insert("car")
Words.insert("hello")
