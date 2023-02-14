#All pairs shortest path Belman Ford algorithm implementation using adjacency lists.

    
class Node:
    
    def __init__(self, val) -> None:
        self.val = val
        self.edges = []

class Graph:
    
    def __init__(self, size) -> None:
        self.nodes = {}
        self.size = size
        
        
    def populate_graph(self, arr):
        for edge in arr:
            node1= edge[0]
            node2= edge[1]
            val = edge[2]
            self.nodes[node1] = self.nodes[node1] if node1 in self.nodes.keys() else self.create_node(node1)
            self.nodes[node2] = self.nodes[node2] if node2 in self.nodes.keys() else self.create_node(node2)
            self.nodes[node2].edges.append((node1, val)) #this is tracking all the edges for which node 2 is the HEAD, because we need the final hop.
                
    def create_node(self, node_val):
        new_node = Node(node_val)
        return new_node 
    
    

    
def belman_ford(graph, src):
    size = graph.size
    inf = 1e10
    init = [inf for i in range(size)]
    init[src-1] = 0  
    arr = [init]
    tru = 0
    # i represents the edge budget
    for i in range(1, size+2):
        
        if i == size+1:
            #checking for negative cycles by going one extra step
            for n in range(1, size+1):
                if arr[size-1][n-1] > arr[size][n-1]:
                    tru +=1
            if tru >0:
                return "negative cycle"
            
        empty = []
        for v in range(1, size+1):
            # i-1 represent last iteration, v-1 is the index as everything is indexed from 1
            last = arr[i-1][v-1]
            mini = inf
            #looking at the edges of the last hop. 
            for hop in graph.nodes[v].edges:
                if arr[i-1][hop[0]-1]+hop[1] < mini:
                    mini = arr[i-1][hop[0]-1]+hop[1]
            empty.append(min(last,mini))
        arr.append(empty)
        
        #checking if the array of A[i,v] == A[i-1,v] are the same and if so it terminates early with the last array. 
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
    
    with open("g3.txt", "r", encoding="utf-8") as file:
        arr = list([int(i) for i in elem.split(" ")] for elem in file.read().strip().splitlines())
        graph = Graph(arr[0][0])
        graph.populate_graph(arr[1:])
        apsp_arr = []
        for i in range(1, graph.size+1):
            apsp_arr.append(belman_ford(graph, i))
            if apsp_arr[0] == 'negative cycle':
                print('negative cycle')
                return "negative cycle"
        
        shortest = 1e10
        for row in apsp_arr:
            row = sorted(row)
            if shortest > row[0]:
                shortest = row[0]

        print((apsp_arr,shortest))
        return apsp_arr
                
        

if __name__ == "__main__":
    main()  