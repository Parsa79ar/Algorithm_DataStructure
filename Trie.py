class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def addWord(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = TrieNode(letter)
            cur_node = cur_node.children[letter]
        cur_node.isEndOfWord = True

    def doesWordExist(self, word):
        if word == "":
            return True
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                return False
            cur_node = cur_node.children[letter]
        return cur_node.isEndOfWord

trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
    trie.addWord(word)

print(trie.doesWordExist("wait")) #True
print(trie.doesWordExist("")) #True
print(trie.doesWordExist("waite")) #False
print(trie.doesWordExist("shop")) #True
print(trie.doesWordExist("shoppp")) #False





# class Trie:
#     def __init__(self):
#         self.root = {"*": "*"}

#     def addWord(self, word):
#         cur_node = self.root
#         for letter in word:
#             if letter not in cur_node:
#                 cur_node[letter] = {}
#             cur_node = cur_node[letter]
#         cur_node["*"] = "*"

#     def doesWordExist(self, word):
#         cur_node = self.root
#         for letter in word:
#             if letter not in cur_node:
#                 return False
#             cur_node = cur_node[letter]
#         return "*" in cur_node
