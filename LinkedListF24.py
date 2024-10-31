class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self,data,index=-1):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        elif index == -1:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        elif index <= self.size:
            new_node = Node(data)
            current_node = self.head
            current_index = 0
            while index - 1 > current_index:
                current_node = current_node.next
                current_index += 1
            new_node.next = current_node.next
            current_node.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.size += 1

    def search(self,data):
        index = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def remove(self,index):
        current_index = 0
        current_node = self.head
        while current_node is not None:
            if current_index == index-1:
                current_node.next = current_node.next.next
            current_node = current_node.next
            current_index += 1


    def __str__(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data)
            result += " -> "
            current_node = current_node.next
        return result

node1 = Node("my")
node2 = Node("name")
node3 = Node("is")
node1.next = node2
node2.next = node3
print(node1.data)
print(node1.next.data)
print(node2.next.data)

my_list = LinkedList()
my_list.insert("my")
my_list.insert("name")
my_list.insert("is")
my_list.insert("Nuri")
print(my_list)

print(my_list.search(5))
print(my_list.search("name"))
print(my_list.search("Nuri"))

my_list.remove(4)
print(my_list)