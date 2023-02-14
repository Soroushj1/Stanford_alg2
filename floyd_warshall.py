   
def floyd_warshall(adj_matrix):
    # this algorithm finds the shortest path by checking the shortest path going through another vortex vs going there directly. If there is no direct path, then we set that to infinity. 
    # So, we start by constructing the first matrix of all pair shortest paths where we pick the min between going through vortex 1 or going to destination directly (if there is no path this is set to infinity).
    # Then, from this matrix, we construct the second matrix graph going through vortex 2 vs going through vortex 1 or directly. Then we construct the thrid matrix going through vortex 3 vs going through vortex 1 or 2 or directly. 
    # You can see how this is building the solution from prior matrices we calculated which is the dynamic programming recurrance paradigm.
    
    
    size = len(adj_matrix)
    out_arr = []
    
    out_arr.append(adj_matrix)
    for k in range(1, size):
        row = []
        for i in range(0, size):
            col = []
            for j in range(0, size):
                # recurrance: 
                case1 = out_arr[k-1][i][j]
                case2 = out_arr[k-1][i][k-1] + out_arr[k-1][k-1][j]
                col.append(min(case1,case2))
            row.append(col)
        out_arr.append(row)
        
    # finding a negative cycle by looking at the diagonal of the matrix
    if len(out_arr) == size:
        for i in range(size): 
            if out_arr[i][i][size-1] < 0:
                return "negative cycle"
    
    shortest = 1e10
    for row in out_arr[-1]:
        row = sorted(row)
        if shortest > row[0]:
            shortest = row[0]
        
        
    return out_arr[-1], shortest
                
def adjacency_matrix(name):
    
    with open(name, "r", encoding="utf-8") as file:
        arr = list([int(i) for i in elem.split(" ")] for elem in file.read().strip().splitlines())
        vor_size, edge_size = arr[0]
        
        adj_matrix = []
        for i in range(vor_size):
            row = []
            for j in range(vor_size):
                if i ==j:
                    row.append(0)
                else:
                    row.append(1e10)
            adj_matrix.append(row)
        
        for edge in arr[1:]:
            a = edge[0]
            b = edge[1]
            c = edge[2]
            adj_matrix[a-1][b-1]= c
                
    return adj_matrix
        
# Answer to assingment: the answers for g1 is negative cycle, g2 is negative cycle, g3 is -19. 
def main():
    
    adj_matrix = adjacency_matrix("g1.txt")
    results=floyd_warshall(adj_matrix)
    print(results)
    return results
                


if __name__ == "__main__":
    main()  