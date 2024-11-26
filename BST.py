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

