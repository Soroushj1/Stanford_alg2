from itertools import combinations
from math import sqrt
from functools import reduce
import numpy as np


def adjacency_matrix(name):
    
    with open(name, "r", encoding="utf-8") as file:
        arr = list([float(i) for i in elem.split(" ")] for elem in file.read().strip().splitlines())
        num = int(arr[0][0])
        arr = arr[1:]
        
        adj_matrix = []
        for i in range(num):
            col = []
            for j in range(num):
                if i != j:
                    col.append(sqrt((arr[i][0]-arr[j][0])**2 + (arr[i][1] - arr[j][1])**2))
                else:
                    col.append(0)
            adj_matrix.append(col)
                    
    return adj_matrix



def traveling_salesman(adj_mat, start):
    
    num = len(adj_mat)
    all_visited = (1 << num)- 1
    inf = np.inf
    # there are 2^n subsets and n destinations. The subsets are encoded with bitmasks so 0101 for example means node 0 and 2 is visited while others are not and it is equal to 5.
    memo = [[None for _ in range(num)] for _ in range(1 << num)]
    # If the subset happens to contain only the start, then the distance is zero
    memo[1 << start][start] = 0
    
    
    
    for end in range(num):
        if end != start:
            # This is the 2D array in the lecture indexed by the subset and the destination (2^n * n)
            # 1 << start | 1 << end is the bitmask of the subset where the start and end are both fliped on to 1 (and everything else to zero - meaning they aren't visited)
            # so we assign the value of the direct edge from our adj_matrix to the memo table.
            print(f"{start},{end}, and {bin(1 << start | 1 << end)}")
            memo[1 << start | 1 << end][end] = adj_mat[start][end]

    
    for size in range(3, num+1):
        for comb in combinations(range(num), size):
            # comb_sum translates the subset (0,1,3) to binary representation of nodes visited which is 1011 and then translates it to integer  which is 2^0 + 2^1 + 2^3 = 7
            comb_sum = sum([1 << i for i in comb])
            if start in comb:
                for j in comb:
                    if j == start:
                        continue
                    min_dist = inf
                    for k in comb:
                        # penultimate vortex k
                        if k == start or k == j:
                            continue
                        # the subset excluding the j
                        subset_without_j = comb_sum ^ (1 << j)
                        # print(f"{j},{k}, and {bin(comb_sum)} {bin(subset_without_j)}")
                        # For a given choice of k, we know the corresponding candidate solution must be a shortest path
                        # from start to k visiting the voteces of subset_without_j combined with the cost of the corresponding final hop
                        # from k to j. Remember that the subproblem of size 2 is already solved above. So, naturally the subset_without_j corresponds to one of them.
                        new_dist = memo[subset_without_j][k] + adj_mat[k][j]
                        if new_dist < min_dist:
                            min_dist = new_dist
                    memo[comb_sum][j] = min_dist
                    
                    
    minCost = inf                 
    for i in range(num):
        if i == start:
            continue
        cost = memo[all_visited][i] + adj_mat[i][start]
        if cost < minCost:
            minCost = cost
    
    return minCost
    

def main():
    adj_mat = adjacency_matrix("tsp.txt")
    print(traveling_salesman(adj_mat,0))
    # the answer is 26442
    

if __name__ == "__main__":
    main()