class Graph:
    def __init__(self, vertices):
        # Number of vertices
        self.V = vertices
        # Dictionary to store adjacency lists
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        # Function to add an edge to the graph
        self.adj[u].append(v)

    def topologicalSort(self):
        # Function to perform Topological Sort
        # Create a list to store in-degree of all vertices
        in_degree = [0] * self.V

        # Traverse adjacency lists to fill in_degree of vertices
        for i in range(self.V):
            for j in self.adj[i]:
                in_degree[j] += 1

        # Create a queue and enqueue all vertices with in-degree 0
        q = []
        for i in range(self.V):
            if in_degree[i] == 0:
                q.append(i)

        # Initialize count of visited vertices
        count = 0

        # Create a list to store topological order
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacent vertices if in-degree of adjacent becomes 0
        while q:
            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = q.pop(0)
            top_order.append(u)

            # Iterate through all its neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for node in self.adj[u]:
                # If in-degree becomes zero, add it to queue
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)

            count += 1

        # Check if there was a cycle
        if count != self.V:
            print("Graph contains cycle")
            return

        # Print topological order
        print("Topological Sort:", top_order)


# Driver code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(5, 4)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(1, 0)
    # g.addEdge(1, 5)

    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()

