graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


visited = set()
bfs(visited, graph, 'A')



#BFS traversal
import queue
class graph:
    def _init_(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
       
    def bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while not(q.empty()):
            current=q.get()
            
            print(current,end=" ")
            visited[current]=True
            
            for i in range(self.nVertices):
                if self.adjMatrix[current][i]>0 and visited[i]==False:
                    visited[i]=True
                    q.put(i)
        return
    
    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] == False:
                self.bfsHelper(i,visited)
               
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
        
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    
    def _str_(self):
        return str(self.adjMatrix)
    
v, e = [int(x) for x in input().split()[:2]]    
g = graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a,b)
g.bfs()


class Graph:
    def _init_(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]
        
    def addEdge(self,v1,v2):
        
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def removeEdge(self,v1,v2):
        if self.containsEdge == False:
            return
        
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def __dfsHelper(self,sv,visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if (self.adjMatrix[sv][i] > 0 and visited[i] == False):
                self.__dfsHelper(i,visited)
                
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)
        
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def _str_(self):
        return str(self.adjMatrix)
    
v, e = [int(x) for x in input().split()[:2]]    
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a,b)
g.dfs()
