class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and node.is_end_of_word

            return False

        _delete(self.root, word, 0)

    def autocomplete(self, prefix):
        def _dfs(node, prefix, results):
            if node.is_end_of_word:
                results.append(prefix)
            for char, child_node in node.children.items():
                _dfs(child_node, prefix + char, results)

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        _dfs(node, prefix, results)
        return results


# Example usage
if __name__ == "__main__":
    trie = Trie()
    words = ["hello", "helium", "hero", "heron", "heritage", "hi", "hippo"]
    for word in words:
        trie.insert(word)

    prefix = "he"
    completions = trie.autocomplete(prefix)
    print(f"Words that start with '{prefix}': {completions}")
    trie.insert("hello")
    trie.insert("helium")

    print(trie.search("hello"))  # True
    print(trie.search("hel"))  # False
    print(trie.starts_with("hel"))  # True
    print(trie.starts_with("heaven"))  # False

    trie.delete("hello")
    print(trie.search("hello"))  # False
    print(trie.search("helium"))# True
    trie.insert("mapping")
    trie.insert("map")
    trie.delete("mapping")
    print(trie.search("map"))