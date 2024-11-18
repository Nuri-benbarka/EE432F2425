from operator import index


class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        result = ""
        cur_node = self
        while cur_node is not None:
            result += str(cur_node.value)
            result += "->"
            cur_node = cur_node.next
        return result[:-2]

class HashTable:
    def __init__(self, size,base=37):
        self.size = size
        self.items = [None for _ in range(size)]
        self.base = base
        self.n_items = 0
        self.threshold = 0.7
        self.resize_factor = 2

    def rehashing(self):
        old_list = self.items
        self.items =[None for _ in range(self.size*self.resize_factor)]
        self.size *= self.resize_factor
        self.n_items = 0

        for i in old_list:
            cur_node = i
            while cur_node is not None:
                k = cur_node.key
                v = cur_node.value
                self.insert(k,v)
                cur_node = cur_node.next

    def hashf(self, key):
        key = str(key)
        index = 0
        for i, k in enumerate(key):
            index += ord(k) * self.base**i
        return index % self.size

    def insert(self, key, value):
        i = self.hashf(key)
        current_node = self.items[i]
        if current_node is None:
            new_node = Node(key, value)
            self.items[i] = new_node
        else:
            while current_node.next is not None:
                if current_node.key == key:
                    current_node.value = value
                    return
                else:
                    current_node = current_node.next
            new_node = Node(key, value)
            current_node.next = new_node
        self.n_items += 1
        load_factor = self.n_items / self.size
        if load_factor > self.threshold:
            self.rehashing()

    def get(self,key):
        i = self.hashf(key)
        cur_node = self.items[i]
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next
        return None

    def delete(self,key):
        i = self.hashf(key)
        cur_node = self.items[i]
        if cur_node.key == key:
            self.items[i] = cur_node.next
        else:
            while cur_node.next is not None:
                if cur_node.next.key == key:
                    cur_node.next = cur_node.next.next
                    break
                cur_node = cur_node.next







my_hash_table = HashTable(5)
my_hash_table.insert(12, 12)
my_hash_table.insert("abc", "abc")
my_hash_table.insert(15, 15)
my_hash_table.insert("EE432", 63)
my_hash_table.insert(22,22)
print(my_hash_table.items)

print(my_hash_table.get(22))
print(my_hash_table.get("EE432"))
print(my_hash_table.get(15))
print(my_hash_table.get(2))

my_hash_table.delete(22)
print(my_hash_table.items)
my_hash_table.delete(15)
print(my_hash_table.items)
my_hash_table.delete("EE432")
print(my_hash_table.items)
my_hash_table.delete("abc")
print(my_hash_table.items)
my_hash_table.delete(12)
print(my_hash_table.items)


