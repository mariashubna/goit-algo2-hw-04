from trie import Trie


class Homework(Trie):

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")
        # збираємо всі слова з Trie у список all_words за допомогою рекурсії
        all_words = []
        self._collect_words(self.root, "", all_words)
        # рахуємо, скільки зібраних слів закінчуються на заданий суфікс pattern, якщо немає - то сума 0
        return sum(1 for word in all_words if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return False
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    print(trie.count_words_with_suffix("e"))
    assert trie.count_words_with_suffix("ion") == 1  # application
    print(trie.count_words_with_suffix("ion"))
    assert trie.count_words_with_suffix("a") == 1  # banana
    print(trie.count_words_with_suffix("a"))
    assert trie.count_words_with_suffix("at") == 1  # cat
    print(trie.count_words_with_suffix("at"))
    print("--------------------------------------------------------")

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    print(trie.has_prefix("app"))
    assert trie.has_prefix("bat") == False
    print(trie.has_prefix("bat"))
    assert trie.has_prefix("ban") == True  # banana
    print(trie.has_prefix("ban"))
    assert trie.has_prefix("ca") == True  # cat
    print(trie.has_prefix("ca"))

    print("Усі тести пройдено успішно.")
