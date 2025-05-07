from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            raise ValueError("Input must be a list of strings")
        if not strings:
            return ""

        for s in strings:
            self.put(s)

        prefix = ""
        node = self.root
        while node and len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print(trie.find_longest_common_word(strings))


print("Усі тести пройдено успішно.")
