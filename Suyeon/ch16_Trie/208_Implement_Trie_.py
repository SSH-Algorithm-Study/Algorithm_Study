import collections

class TreeNode:
    def __init__(self):
        self.children = {}  # 다음단어 : TreeNode()
        self.end = False  # 단어의 끝임을 나타내주는

class Trie:

    def __init__(self):
        self.trie = TreeNode()


    def insert(self, word: str) -> None:
        p = self.trie

        for char in word:
            if char not in p.children:  # 자식중에 있다면 그대로 넘어감
                p.children[char] = TreeNode()
            p = p.children[char]

        p.end = True

    def search(self, word: str) -> bool:
        p = self.trie

        for char in word:
            if char not in p.children:  # 있는지 없는지 조사
                return False
            p = p.children[char]

        return p.end == True  # 단어의 마지막 문자여야한다


    def startsWith(self, prefix: str) -> bool:
        p = self.trie

        for char in prefix:
            if char not in p.children:
                return False
            p = p.children[char]

        return True