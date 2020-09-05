from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def findParent(self, parent, i):
        if(parent[i] == i):
            return i
        return self.findParent(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.findParent(parent, x)
        yroot = self.findParent(parent, y)

        if(rank[xroot] < rank[yroot]):
            parent[xroot] = yroot
        elif(rank[xroot] < rank[yroot]):
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def krushkalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key = lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while(e < (self.V - 1)):
            u, v, w = self.graph[i]
            i += 1
            x = self.findParent(parent, u)
            y = self.findParent(parent, v)

            if(x != y):
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Following are the edges in the constructed MST")
        for u,v,w in result:
            print("{}--{} = {}".format(u, v, w))
    
g = Graph(4)
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
g.krushkalMST()