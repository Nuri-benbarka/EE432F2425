class ArrayBST:
    def __init__(self, capacity):
        self.tree = [None] * capacity  # Initialize an array to store the BST nodes
        self.capacity = capacity

    def insert(self, key):
        if self.tree[0] is None:
            self.tree[0] = key  # Insert at root if tree is empty
        else:
            self._insert(0, key)

    def _insert(self, index, key):
        if index >= self.capacity:
            raise IndexError("Tree capacity exceeded")

        if self.tree[index] is None:
            self.tree[index] = key
        elif key < self.tree[index]:
            left_index = 2 * index + 1
            self._insert(left_index, key)
        elif key > self.tree[index]:
            right_index = 2 * index + 2
            self._insert(right_index, key)

    def search(self, key):
        return self._search(0, key)

    def _search(self, index, key):
        if index >= self.capacity or self.tree[index] is None:
            return None
        if self.tree[index] == key:
            return index
        elif key < self.tree[index]:
            return self._search(2 * index + 1, key)
        else:
            return self._search(2 * index + 2, key)

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self._delete(index)

    def _delete(self, index):
        if self.tree[index] is None:
            return

        if self.tree[2 * index + 1] is None and self.tree[2 * index + 2] is None:
            self.tree[index] = None
        elif self.tree[2 * index + 1] is None:
            self.tree[index] = self.tree[2 * index + 2]
            self._delete(2 * index + 2)
        elif self.tree[2 * index + 2] is None:
            self.tree[index] = self.tree[2 * index + 1]
            self._delete(2 * index + 1)
        else:
            min_larger_index = self._min_value_index(2 * index + 2)
            self.tree[index] = self.tree[min_larger_index]
            self._delete(min_larger_index)

    def _min_value_index(self, index):
        while 2 * index + 1 < self.capacity and self.tree[2 * index + 1] is not None:
            index = 2 * index + 1
        return index

    def __repr__(self):
        if not any(self.tree):
            return '<empty tree>'
        return '\n'.join(self._build_tree_string(0, 0))

    def _build_tree_string(self, index, depth):
        result = []
        if index < self.capacity and self.tree[index] is not None:
            node_repr = f"{' ' * (depth * 2)}[{index}]: {self.tree[index]}"
            result.append(node_repr)
            result.extend(self._build_tree_string(2 * index + 1, depth + 1))
            result.extend(self._build_tree_string(2 * index + 2, depth + 1))
        return result


# Example usage
if __name__ == "__main__":
    bst = ArrayBST(15)  # Array-based BST with capacity for 15 nodes
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("BST Representation:\n", bst)

    # Search for a key
    key = 40
    index = bst.search(key)
    if index is not None:
        print(f"Key {key} found in BST at index {index}.")
    else:
        print(f"Key {key} not found in BST.")

    # Delete a key
    bst.delete(20)
    print("BST Representation after deleting 20:\n", bst)

    bst.delete(30)
    print("BST Representation after deleting 30:\n", bst)

    bst.delete(50)
    print("BST Representation after deleting 50:\n", bst)
