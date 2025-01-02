class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError('pop from an empty heap')
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._sift_down(0)
        return item

    def _sift_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            self._sift_up(parent)

    def _sift_down(self, index):
        child = 2 * index + 1
        if child >= len(self.heap):
            return
        if child + 1 < len(self.heap) and self.heap[child + 1][0] < self.heap[child][0]:
            child += 1
        if self.heap[index][0] > self.heap[child][0]:
            self._swap(index, child)
            self._sift_down(child)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __len__(self):
        return len(self.heap)


def get_shortest_path(previous, start_vertex, end_vertex):
    path = []
    current_vertex = end_vertex
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous[current_vertex]
    if path[0] == start_vertex:
        return path
    else:
        return None  # No path found


class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))  # For undirected graph

    def dijkstra(self, start_vertex, end_vertex=None):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        distances[start_vertex] = 0
        priority_queue = MinHeap()
        priority_queue.push((0, start_vertex))

        while len(priority_queue) > 0:
            current_distance, current_vertex = priority_queue.pop()

            if current_vertex == end_vertex:
                break

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    priority_queue.push((distance, neighbor))

        return distances, previous


# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 4)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('D', 'E', 3)
    graph.add_edge('B', 'E', 3)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('A', 'E', 8)

    start_vertex = 'A'
    distances, previous = graph.dijkstra(start_vertex)

    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    print("\nShortest paths:")
    for vertex in graph.vertices:
        if vertex != start_vertex:
            path = get_shortest_path(previous, start_vertex, vertex)
            if path:
                print(f"Path to {vertex}: {' -> '.join(path)}")
            else:
                print(f"No path to {vertex}")

    distances, previous = graph.dijkstra('D', 'C')
    print(distances)
    print(distances['C'])
