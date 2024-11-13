class Queue:
    def __init__(self, size):
        self.items = [None for _ in range(size)]
        self.front = -1
        self.back = -1
        self.n_items = 0

    def enque(self,data):
        if self.back == -1 and self.front==-1:
            self.back = 0
            self.front = 0
            self.items[self.back] = data
            self.n_items += 1
        elif (self.back + 1) % len(self.items) != self.front:
            self.back += 1
            self.back %= len(self.items)
            self.items[self.back] = data
            self.n_items += 1
        else:
            raise IndexError("queue overflow")

    def dequeue(self):
        if self.back == -1 and self.front == -1:
            raise IndexError("empty queue")
        elif self.back == self.front:
            data = self.items[self.front]
            self.back = self.front = -1
            self.n_items -= 1
            return data
        else:
            data = self.items[self.front]
            self.front += 1
            self.front %= len(self.items)
            self.n_items -= 1
            return data

    def __str__(self):
        if self.back == -1 and self.front == -1:
            return "<empty queue>"
        else:
            strng = "["
            f = self.front
            while f != self.back:
                strng += str(self.items[f])
                strng += ", "
                f += 1
                f %= len(self.items)
            strng += str(self.items[f])
            strng += "]"
            return strng


my_queue = Queue(5)
my_queue.enque(7)
my_queue.enque(5)
my_queue.enque(3)
my_queue.enque(1)
print(my_queue)
print(my_queue.n_items)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue)
print(my_queue.n_items)
my_queue.enque(-1)
my_queue.enque(-3)
my_queue.enque(-5)
# my_queue.enque(-7)  queue overflow
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue)
print(my_queue.dequeue())
print(my_queue.dequeue())
# print(my_queue.dequeue()) queue empty