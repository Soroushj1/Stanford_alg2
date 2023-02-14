#All pairs shortest path Belman Ford algorithm implementation using adjacency lists.
from dijkstar import Graph, find_path


class Node:
    
    def __init__(self, val) -> None:
        self.val = val
        self.edges = []

class My_Graph:
    
    def __init__(self, size) -> None:
        self.nodes = {}
        self.size = size
        
    def create_node(self, node_val):
        new_node = Node(node_val)
        return new_node 
        
    def populate_graph(self, arr):
        for edge in arr:
            node1= edge[0]
            node2= edge[1]
            val = edge[2]
            self.nodes[node1] = self.nodes[node1] if node1 in self.nodes.keys() else self.create_node(node1)
            self.nodes[node2] = self.nodes[node2] if node2 in self.nodes.keys() else self.create_node(node2)
            self.nodes[node2].edges.append((node1, val)) #this is tracking all the edges for which node 2 is the HEAD, because we need the final hop.
            
    def add_johnsons_weights(self):
        for node in self.nodes.keys():
            self.nodes[node].edges.append((self.size+1, 0))
        self.nodes[self.size+1] = self.create_node(self.size+1)
            
                
    
def belman_ford(graph, src):
    size = graph.size
    inf = 1e10
    init = [inf for i in range(size)]
    init[src-1] = 0  
    arr = [init]
    tru = 0
    for i in range(1, size+2):
        
        # checking for negative cycles by going one extra step
        if i == size+1:
            for n in range(1, size+1):
                if arr[size-1][n-1] > arr[size][n-1]:
                    tru +=1
            if tru >0:
                return "negative cycle"
            
        empty = []
        for v in range(1, size+1):
            last = arr[i-1][v-1]
            mini = inf
            #looking at the edges of the last hop. 
            for hop in graph.nodes[v].edges:
                if arr[i-1][hop[0]-1]+hop[1] < mini:
                    mini = arr[i-1][hop[0]-1]+hop[1]
            empty.append(min(last,mini))
        arr.append(empty)
        
        # checking if the array of A[i,v] == A[i-1,v] are the same and if so it terminates early with the last array. 
        for n in range(1, size+1):
            if arr[i][n-1] == arr[i-1][n-1]:
                tru +=1
        if tru == size:
            return arr[-1]
        else:
            tru = 0
        
    return arr[-1]
            
     
            

# Answer to assingment: the answers for g1 is negative cycle, g2 is negative cycle, g3 is -19.
def main():
    
    with open("APSP-test.txt", "r", encoding="utf-8") as file:
        arr = list([int(i) for i in elem.split(" ")] for elem in file.read().strip().splitlines())
        vor_size, edge_size = arr[0]
        
        my_graph_cp = My_Graph(vor_size)
        my_graph_cp.populate_graph(arr[1:])
        
        my_graph = My_Graph(vor_size)
        my_graph.populate_graph(arr[1:])
        my_graph.add_johnsons_weights()
        my_graph.size = len(my_graph.nodes)
        
        negative_cycle=belman_ford(my_graph_cp,my_graph_cp.size)
        
        if negative_cycle == 'negative cycle':
            print('negative cycle')
            return negative_cycle
        
        reweight=belman_ford(my_graph, my_graph.size)
        new_arr= []
        for edge in arr[1:]:
            node1= edge[0]
            node2= edge[1]
            val = edge[2]
            cprime = val + reweight[node1-1] - reweight[node2-1]
            new_arr.append([node1, node2, cprime])
        
        graph = Graph()
        for edge in new_arr:
            graph.add_edge(edge[0],edge[1],edge[2])
            
        shortest_paths = []
        for i in range(1, vor_size+1):
            col = []
            for j in range(1, vor_size+1):
                col.append(find_path(graph,i,j).total_cost-reweight[i-1]+reweight[j-1])
            shortest_paths.append(col)

        
        shortest = 1e10
        for row in shortest_paths:
            row = sorted(row)
            if shortest > row[0]:
                shortest = row[0]

        print((shortest_paths,shortest))
        return shortest_paths
                

if __name__ == "__main__":
    main()  