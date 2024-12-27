class MaxHeap:
    def __init__(self, capacity):
        self.tree = [None] * capacity  # Initialize an array to store the BST nodes
        self.capacity = capacity
        self.last_ele_index = -1

    def insert(self, value):
        if self.last_ele_index + 1 >= self.capacity:
            print("heap overflow")
        else:
            self.last_ele_index += 1
            self.tree[self.last_ele_index] = value
            i = self.last_ele_index
            while i > 0:
                if self.tree[i] > self.tree[(i-1)//2]:
                    self.tree[i], self.tree[(i - 1) // 2] = self.tree[(i-1)//2], self.tree[i]
                    i = (i - 1) // 2
                else:
                    break

    def max(self):
        return self.tree[0]


    def delete(self):
        if self.last_ele_index == -1:
            print("empty heap")
        elif self.last_ele_index == 0:
            item = self.tree[0]
            self.tree[0] = None
            self.last_ele_index -= 1
            return item
        else:
            item = self.tree[0]
            self.tree[0] = self.tree[self.last_ele_index]
            self.tree[self.last_ele_index] = None
            self.last_ele_index -= 1
            i = 0
            while i <= self.last_ele_index:
                if self.tree[i*2+2] is not None:
                    if self.tree[i*2+1] > self.tree[i*2+2]:
                        if self.tree[i*2+1]> self.tree[i]:
                            self.tree[i * 2 + 1] , self.tree[i]= self.tree[i], self.tree[i*2+1]
                            i = i * 2 + 1
                        else:
                            break
                    else:
                        if self.tree[i*2+2] > self.tree[i]:
                            self.tree[i * 2 + 2], self.tree[i] = self.tree[i], self.tree[i * 2 + 2]
                            i = i * 2 + 2
                        else:
                            break
                elif self.tree[i*2+1] is not None:
                    if self.tree[i * 2 + 1] > self.tree[i]:
                        self.tree[i * 2 + 1], self.tree[i] = self.tree[i], self.tree[i * 2 + 1]
                        i = i * 2 + 1
                    else:
                        break
                else:
                    break
            return item


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
    my_heap = MaxHeap(7)  # Array-based BST with capacity for 15 nodes
    my_heap.insert(50)
    my_heap.insert(30)
    my_heap.insert(20)
    my_heap.insert(40)
    my_heap.insert(70)
    my_heap.insert(60)
    my_heap.insert(80)
    my_heap.insert(80)

    print("BST Representation:\n", my_heap)

    # Delete a key
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
