class Graph:
    def __init__(self, V):
        self.adjList = [[] for _ in range(V)]
        self.V  = V

    def addEdge(self, x, y):
        #self.adjList[x].append(y)
        self.adjList[y].append(x) # Depends how they are provided (the direction of the arrow)
    
    def BFS(self, start):
        visited = [False for _ in range(self.V)]
        # layer = [0 for _ in range(self.V)]
        # parent = [i for i in range(self.V)]
        queue = []

        # Mark the starting vertex as visited
        visited[start] = True
        # layer[start] = 0
        counter = 0

        # Enqueue starting vertex
        queue.append(start)
        while (len(queue) != 0):
            counter += 1
            v = queue.pop(0)
            for u in self.adjList[v]:
                if not visited[u]:
                    visited[u] = True
                    # layer[u] = layer[v] + 1
                    # parent[u] = v
                    queue.append(u)
        return counter

    def __str__(self) -> str:
        return str(self.adjList)
    
N, M = map(int, input().split())

graph = Graph(N)
for _ in range(M):
    x, y = map(int, input().split())
    graph.addEdge(x-1, y-1) # -1 Only if they sart with node 1

print(graph.BFS(0))
