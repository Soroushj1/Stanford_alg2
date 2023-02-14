from itertools import combinations
import re 
from collections import defaultdict
from networkx.utils import UnionFind


class MyUnionFind:
    
    def __init__(self, size, data ) -> None:
        self.parent = list(i for i in data) 
        self.parentMap = {val: i for i, val in enumerate(data)}
        self.rank = [0 for i in range(size)]
        
    
    def find(self, point: int) -> int:
        index = self.parentMap[point] 
        root = point 
        while self.parent[index] != root:
            self.parent[index] = self.parent[self.parentMap[self.parent[index]]]
            root = self.parent[index]
            
        return root
    
    def union(self, point1: int, point2: int) -> int:
        
        s1 = self.find(point1)
        s2 = self.find(point2)
        s1_index = self.parentMap[s1]
        s2_index = self.parentMap[s2]
        
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
        for i, val in enumerate(self.parent):
            if self.parentMap[val] == i:
                clusters.append(val)
        return len(clusters)


def make_bitMasks():
    
    hamming_0 = [0]
    hamming_1 =  [1 << i for i in range(24)]
    hamming_2 = []
    for i,j in combinations(range(24),2):
        a = 1 << i 
        b = 1 << j
        hamming_2.append(a ^ b)
        
    # alternative for generating hamming2, 276 combinations (24 choose 2. 
    # for j in range(len(hamming_1)):
    #     for k in range(j+1, len(hamming_1)):
    #         print("{0:b}".format(hamming_1[k] ^ hamming_1[j]))
    
    return hamming_0, hamming_1, hamming_2

        
    
        
def read_file_to_arr(file):
    node_set = set()
    dict = defaultdict(int, default_factory = None)
    with open(file, "r", encoding="utf-8") as file:
        for i, val in enumerate(file.read().strip().splitlines()):
            if i !=0:
                binToInt = int("".join(re.findall(r"\d\S*", val)), 2)
                node_set.add(binToInt)
        arr = list(node_set)       
        dict = {val:i for i, val in enumerate(arr)}

    return arr, dict

        
def main():
    
    file_name = "clustering_big.txt"
    intArr, intDict = read_file_to_arr(file_name)
    hamming_0, hamming_1, hamming_2 = make_bitMasks()
    hamming = hamming_0+hamming_1+hamming_2
    Mycluster = MyUnionFind(200000, intArr)
    cluster =  UnionFind(intArr)
    
    
    for i in hamming:
        for j in intArr:
            xor = i ^ j
            if xor in intDict.keys():
                Mycluster.union(intArr[intDict[xor]], j)
                cluster.union(intArr[intDict[xor]], j)
                   
    print(Mycluster.get_clusters())     # answer with my implementation of UnionFind        
    
    groups = []
    for i in cluster.to_sets():
        groups.append(i)
    print(len(groups)) # answer with python networkx.utils implementation of UnionFind
        
if __name__ == "__main__":
    main()
        