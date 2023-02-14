

class UnionFind:
    
    def __init__(self, size) -> None:
        self.size = size #number of clusters, in the beginning set to all the size of nodes
        self.parent = [i for i in range(1, size+1)] #array of parents in the beginning [0,1,2,3,4]. Meaning 0 is parent of zero and so on. 
        self.rank = [0 for i in range(1, size+1)] #rank of each [0,0,0,0,0]
        
    
    def find(self, point: int) -> int:
        index = point-1 # 1 translates to index 0
        root = point 
        while self.parent[index] != root:
            self.parent[index] = self.parent[self.parent[index]-1]
            root = self.parent[index]
            
        return root
    
    def union(self, point1: int, point2: int) -> int:
        
        s1 = self.find(point1)
        s2 = self.find(point2)
        s1_index = s1-1
        s2_index = s2-1
        
        if s1 == s2: #root is the same, not doing the union
            return 0
        else:
            if self.rank[s1_index] != self.rank[s2_index]:
                if self.rank[s1_index] > self.rank[s2_index]:
                    self.parent[s2_index] =self.parent[s1_index]
                else:
                    self.parent[s1_index] =self.parent[s2_index]
            else:
                self.parent[s2_index] =self.parent[s1_index] # arbitrary
                self.rank[s1_index] =  self.rank[s2_index] + 1
        return 1
    
    #counts the number of clusters based on the number of leaders. For example if initially
    # [1,2,3,4,5] was the parent array (everyone is its own parent). Then we have 5 clusters
    # [1,1,1,1,5], we have 2 clusters 1 and 5. 
    def get_clusters(self)-> int:
        clusters = []
        for i in range(len(self.parent)):
            if self.parent[i] == i+1:
                clusters.append(i+1)
        return len(clusters)
            
def read_file(name):
    
    with open(name, "r", encoding="utf-8") as file:
        arr = list([int(j) for j in i.split(' ')] 
                   for i in file.read().strip().splitlines())
    return arr
    


def main():
    
   arr = read_file("clustering.txt")
   size = arr[0][0]
   sorted_arr = sorted(arr[1:], key= lambda x: x[-1])
   cluster = UnionFind(size)
   
   i = 0
   final_distance = 0
   while cluster.get_clusters() > 3 :
        cluster.union(sorted_arr[i][0], sorted_arr[i][1])
        final_distance = sorted_arr[i][2]
        i+=1
        
   print(final_distance)
        
    
   
    

if __name__ == "__main__":
    main()