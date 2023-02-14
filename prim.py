from collections import defaultdict
import heapq

class Graph:
    
    def __init__(self):
        self.nodes = defaultdict(list)
        
    def populate_graph(self, arr):
        for elem in arr:
            #The edges for each vortex are saved in a heap in a symetrical fashion so that node 1 has node 2 and node 2 has node 1. 
            # Obviously adding it to a minHeap, ensures we are picking the minimum edge cost everytime we pop the minimum
            heapq.heappush(self.nodes[elem[0]],(elem[2], elem[1]))
            heapq.heappush(self.nodes[elem[1]], (elem[2], elem[0]))



# This Prim's minimum spanning tree algorithm is implemented with having edges in the heap
# as oppose to the alternative vortex being saved in heap impelementation in Dijkstra. 
def mst(graph):
    cost = 0
    i = 1 # arbitrary seed vortex. 
    tree = [i]
    front = [heapq.heappop(graph.nodes[i])] 
    cost = 0
    while len(tree) < len(graph.nodes): #The length of a tree in a minimum spanning tree is smaller than the number of nodes. 
        weight, next_index = heapq.heappop(front)
        cost += weight
        tree.append(next_index)
        front =[]
        for i in tree:
            # removing all the edges that have their head in the Tree already
            while graph.nodes[i] and graph.nodes[i][0][1] in tree:
                heapq.heappop(graph.nodes[i])
            # Then, adding to the frontier the minimum edge that has a head outside the exsiting Tree. 
            if graph.nodes[i] and graph.nodes[i][0] not in front:
                heapq.heappush(front,graph.nodes[i][0])   
    return tree, cost
        


def main():
    
    with open("edges.txt","r",encoding="utf-8") as file:
        arr = list([int(v) for v in e.split(' ')] for e in file.read().strip().splitlines())
        node_size, edge_size = arr[0]
        graph = Graph()
        graph.populate_graph(arr[1:])
        tree, cost = mst(graph)
        return tree, cost
print(main())
    

if __name__ == "__main__":
    main()