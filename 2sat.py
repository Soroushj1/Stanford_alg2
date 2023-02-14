from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)


class Graph:
    
    def __init__(self, v):
        self.v = v 
        self.graph = defaultdict(list)
        self.graph_trans = None
        
    
    def add_edge(self, edge):
        self.graph[edge[0]].append(edge[1])
    
    
    def make_trans(self):
        graph_trans = Graph(self.v)
        for key in self.graph.keys():
            for node in self.graph[key]:
                graph_trans.add_edge((node,key))
        self.graph_trans = graph_trans
    
    
    def finishing_time(self) -> list:
        visited = {}
        stack = []
        n = self.v
        for v in range(n, -n-1, -1):
            visited[v] = False
            
        for v in range(n, -n-1, -1):
            if visited[v] is False and v != 0:
                self.dfs(self.graph_trans.graph, visited, v, stack)
                
        return stack
                
                
    def dfs(self, graph, visited, v, stack):
        visited[v] = True
        for edge in graph[v]:
            if visited[edge] is False:
                self.dfs(graph, visited, edge,stack)
        # if the src vortex does have any edges or they are all visited, then it adds it to the stack
        stack.append(v)
            
        

    def two_sat(self):
        
        n =self.v
        scc = []
        components = []
        ftime = self.finishing_time()
        visited = {}
        for v in range(n,-n-1,-1):
            visited[v] = False
            
        for v in ftime[::-1]:
            if visited[v] is False:
                self.dfs(self.graph, visited, v, scc)
            components.append(scc)
            for v in scc:
                if -1*v in scc:
                    return False
            scc = []
            
        return True
        
        

def construct_graphs(clauses,num):

    graph = Graph(num)
    for clause in clauses:
        edge1 = (clause[0]*-1, clause[1])
        edge2 = (clause[1]*-1, clause[0])
        graph.add_edge(edge1)
        graph.add_edge(edge2)
        
    graph.make_trans() 
    return graph
    

def read_file(file_name):
    clause = []
    num = 0
    with open(file_name, "r", encoding="utf-8") as file:
        arr = [i for i in file.read().strip().splitlines()]
        for i in range(len(arr)):
            if i == 0:
                num=int(arr[i])
                continue
            clause.append(tuple(int(j) for j in arr[i].split(" ")))
    
    return clause, num
        

def main():
    
    clauses, num = read_file("2sat6.txt")

    graph= construct_graphs(clauses,num)
    print(graph.two_sat())

if __name__ == "__main__":
    main()