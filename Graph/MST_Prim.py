class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)]
                                          for row in range(vertices)]

    def minKey(self, mstSet, key):
        minDist = float('inf')
        minVertex = None

        for vrtx in range(self.V):
            if(key[vrtx] <= minDist and mstSet[vrtx] == False):
                minDist = key[vrtx]
                minVertex = vrtx

        return minVertex

    def primMST(self):
        mstSet = [False] * self.V
        key = [float('inf')] * self.V
        key[0] = 0
        parent = [None] * self.V
        parent[0] = -1

        for v in range(self.V):
            u = self.minKey(mstSet, key)
            mstSet[u] = True

            for v in range(self.V):
                if(self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        print(parent)
        minWeightSum = 0
        for i in range(1, self.V):
            print(parent[i], "-", i, "  ", self.graph[i][ parent[i] ])
            minWeightSum += self.graph[i][ parent[i] ]
        print(minWeightSum)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.primMST()
