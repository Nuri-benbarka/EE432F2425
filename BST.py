class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class BST:
    def __init__(self):
        self.root = None

    def update_height(self,node):
        if node.left is None:
            height_l = 0
        else:
            height_l = node.left.height
        if node.right is None:
            height_r = 0
        else:
            height_r = node.right.height
        return max(height_l,height_r) + 1

    def insert_rec(self,node,value):
        if value >= node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_rec(node.right,value)
                node.right.height = self.update_height(node.right)
        else:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_rec(node.left,value)
                node.left.height = self.update_height(node.left)


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_rec(self.root,value)
            self.root.height = self.update_height(self.root)

    def search_rec(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value > node.value:
            return self.search_rec(node.right,value)
        else:
            return self.search_rec(node.left,value)

    def search(self,value):
        if self.root is None:
            return False
        else:
            return self.search_rec(self.root, value)

    def find_min(self,node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete_rec(self,node,value):
        if value == node.value:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                minimum = self.find_min(node.right)
                node.value, minimum.value = minimum.value, node.value
                node.right = self.delete_rec(node.right, value)
        elif value > node.value:
            node.right = self.delete_rec(node.right,value)
            if node.right is not None:
                node.right.height = self.update_height(node.right)
        elif value < node.value:
            node.left = self.delete_rec(node.left, value)
            if node.left is not None:
                node.left.height = self.update_height(node.left)
        return node


    def delete(self,value):
        if self.root is None:
            raise IndexError
        else:
            self.root = self.delete_rec(self.root, value)
            if self.root is not None:
                self.root.height = self.update_height(self.root)

    def BFS(self):
        q = [self.root]
        while len(q) > 0:
            current_node = q.pop()
            if current_node.right is not None:
                q.append(current_node.right)
            if current_node.left is not None:
                q.append(current_node.left)
            yield current_node.value

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




my_tree = BST()
my_tree.insert(5)
my_tree.insert(3)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(7)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(12)
print(my_tree)
print(my_tree.search(5))
print(my_tree.search(12))
print(my_tree.search(4))
print(my_tree.search(55))
print(my_tree.search(-5))
my_tree.delete(12)
my_tree.delete(2)
my_tree.delete(5)
print(my_tree)

for item in my_tree.BFS():
    print(item, end=" ")

print(" ")
for item in my_tree.inorder():
    print(item, end=" ")

print(" ")
for item in my_tree.preorder():
    print(item, end=" ")

print(" ")
for item in my_tree.postorder():
    print(item, end=" ")

