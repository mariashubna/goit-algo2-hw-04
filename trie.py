class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word, value=None):
        if not isinstance(word, str):
            raise ValueError("Word must be a string")
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True
        node.value = value

    def get(self, word):
        if not isinstance(word, str):
            raise ValueError("Word must be a string")
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end_of_word else None

    def _collect_words(self, node: TrieNode, prefix: str, result: list):
        if node.is_end_of_word:
            result.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, result)
