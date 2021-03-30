"""bellman ford algorithm for finding the shortest path to a vertex from a single sort
this alghorithm handles negative weights"""
class graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def printArray(self, dist):
        print("distance of vertex from the source")
        for i in range(self.V):
            print("%d \t\t %d" %(i, dist[i]))
    def bellmanFord(self, src):
        dist = [float("Inf")]*self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("graph has negative weight cycles")
                return 0
        self.printArray(dist)
        
if __name__=="__main__":
    #note vertices should start from zero
    g = graph(5)
    g.addEdge(0,1,2)
    g.addEdge(0,2,4)
    g.addEdge(1,2,3)
    g.addEdge(1,3,2)
    g.addEdge(1,4,2)
    g.addEdge(3,2,5)
    g.addEdge(3,1,6)
    g.addEdge(4,3,2)
    g.bellmanFord(2)
    
