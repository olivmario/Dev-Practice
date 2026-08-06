class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Autocomplete:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isEnd = True

    def search(self, s):
        result = []
        node = self.root

        for c in s:
            if c not in node.children:
                return result
            node = node.children[c]

        self.dfs(node, s, result)
        return result

    def dfs(self, node, prefix, result):
        if node.isEnd:
            result.append(prefix)

        for c, child in node.children.items():
            self.dfs(child, prefix + c, result)


if __name__ == "__main__":
    autocomplete = Autocomplete()
    words = ["dog", "deer", "deal"]

    for word in words:
        autocomplete.insert(word)

    print(autocomplete.search("de"))
