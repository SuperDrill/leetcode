class Trie:
    class Node:
        def __init__(self):
            self.nodes = {}
            self.val = 'a'
            self.isWord = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.Node();
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                newNode = Trie.Node()
                newNode.val = c
                node.nodes[c] = newNode
                node = newNode
        node.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                return False
        return node.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)