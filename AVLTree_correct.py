class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self, value=None):
        if value is None:
            self.root = None
        else:
            self.root = Node(value)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, B):
        A = B.left
        y = A.right

        # Perform rotation
        A.right = B
        B.left = y

        # Update heights
        B.height = max(self.get_height(B.left), self.get_height(B.right)) + 1
        A.height = max(self.get_height(A.left), self.get_height(A.right)) + 1

        # Return new root
        return A

    def left_rotate(self, A):
        B = A.right
        y = B.left

        # Perform rotation
        B.left = A
        A.right = y

        # Update heights
        A.height = max(self.get_height(A.left), self.get_height(A.right)) + 1
        B.height = max(self.get_height(B.left), self.get_height(B.right)) + 1

        # Return new root
        return B

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        # Perform normal BST insertion
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Update height of this ancestor node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # Get the balance factor
        balance = self.get_balance(node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        # Perform standard BST delete
        if not node:
            return node

        elif value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            temp = self.min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        if node is None:
            return node

        # Update height of this ancestor node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # Get the balance factor
        balance = self.get_balance(node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def BFS(self):
        if self.root is None:
            return None
        our_queue = [self.root]
        while len(our_queue) > 0:
            current_node = our_queue.pop(0)
            if current_node.left is not None:
                our_queue.append(current_node.left)
            if current_node.right is not None:
                our_queue.append(current_node.right)
            yield current_node

    def inorder(self, node="root"):
        if node == "root":
            yield from self.inorder(self.root)
        else:
            if node is not None:
                yield from self.inorder(node.left)
                yield node.value
                yield from self.inorder(node.right)

    def preorder(self, node="root"):
        if node == "root":
            yield from self.preorder(self.root)
        else:
            if node is not None:
                yield node.value
                yield from self.preorder(node.left)
                yield from self.preorder(node.right)

    def postorder(self, node="root"):
        if node == "root":
            yield from self.postorder(self.root)
        else:
            if node is not None:
                yield from self.postorder(node.left)
                yield from self.postorder(node.right)
                yield node.value

    def getTreeString(self, node, level, result):
        result += "   " * level + str(node.value) + "\n"
        if node.left is not None:
            result = self.getTreeString(node.left, level + 1, result)
        if node.right is not None:
            result = self.getTreeString(node.right, level + 1, result)
        return result

    def __repr__(self):
        if self.root is None:
            return "empty tree"
        else:
            return self.getTreeString(self.root, 0, "")


# Example usage
if __name__ == "__main__":
    tree = AVLTree()

    nodes = [10, 11, 20, 21, 30, 31, 40, 41, 50, 25, 51, 26]

    for node in nodes:
        tree.insert(node)
        print(tree)
        print("______________________")
    # Pre-order traversal of the constructed AVL tree
    print("Pre-order traversal of the constructed AVL tree is:")
    for node in tree.preorder():
        print(node, end=" ")
    print()

    print(tree)

    # Deleting node
    tree.delete(31)
    tree.delete(50)
    tree.delete(51)

    print(tree)
