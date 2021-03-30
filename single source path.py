#alireza bagherinia,alireza khorsand,pouya sanaii
"""bellman ford algorithm for finding the shortest path to a vertex from a single sort
this alghorithm handles negative weights"""
def bellmanFord(graph, source):
    distance, predecessor = dict(),dict()
    for node in graph:
        distance[node],predecessor[node] = float("inf"), None
    distance[source] = 0
    for _ in range(len(graph)-1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour]>distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour],node
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "negative weight cycle"
    return distance,predecessor
if __name__=="__main__":
    graph ={'a':{'b': -1, 'c':4},
            'b':{'c':3,'d':2,'e':2},
            'c':{},
            'd':{'b':1,'c':5},
            'e':{'d':-3}}
    distance, predecessor = bellmanFord(graph,'b')
    print(distance)
