class Graph:
    def __init__(self, directed = False):
        self.adjMatrix = []
        self.directed = directed
        self.radius = 0

    def add_node(self):
        num = len(self.adjMatrix)
        for r in self.adjMatrix:
            r.append(0)
        new_row = [0 for _ in range(num+1)]
        self.adjMatrix.append(new_row)

    def add_edge(self,start,end,weight=1):
        self.adjMatrix[start][end]=weight
        if not self.directed:
            self.adjMatrix[end][start] = weight

    def BFS(self,start=0):
        visited = set()
        visited.add(start)
        print(start)
        q = []
        for i,v in enumerate(self.adjMatrix[start]):
            if v != 0 and i not in visited:
                q.append(i)
        while len(visited) < len(self.adjMatrix):
            current_v = q.pop(0)
            if current_v in visited:
                continue
            visited.add(current_v)
            print(current_v)
            for i, v in enumerate(self.adjMatrix[current_v]):
                if v != 0 and i not in visited:
                    q.append(i)



my_graph = Graph()
my_graph.add_node()
my_graph.add_node()
my_graph.add_node()
my_graph.add_node()
my_graph.add_node()
my_graph.add_node()
my_graph.add_node()
print(my_graph.adjMatrix)

my_graph.add_edge(0,1,1)
my_graph.add_edge(0,5,3)
my_graph.add_edge(0,6,6)
my_graph.add_edge(1,2,2)
my_graph.add_edge(2,5,4)
my_graph.add_edge(2,3,2)
my_graph.add_edge(3,4,1)
my_graph.add_edge(4,5,8)
my_graph.add_edge(4,6,2)


print(my_graph.adjMatrix)
my_graph.BFS(0)

