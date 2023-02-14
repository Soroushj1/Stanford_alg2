def knapsack(arr, cap, num):
    
    #Uses one array for previous solution. 
    # The inner for-loop is fliped and whenever the weight drops below the capacity we break out of the for-loop avoiding all the zeros. 
    sack = [0 for _ in range(cap+1)]
    for i in range(1, num+1):
        for x in range(cap,0, -1):
            if x > arr[i-1][1]:
                sack[x]= max(sack[x], sack[x-arr[i-1][1]]+arr[i-1][0])
            else:
                break
    return sack
    

def main():
    
    with open("knapsack.txt", "r", encoding="utf-8") as file:
        arr = list([int(j)for j in i.split(" ")]for i in file.read().strip().splitlines())
        cap = arr[0][0]
        num= arr[0][1]
        sack = knapsack(arr[1:],cap,num)
        print(sack[-1])
        

if __name__ == "__main__":
    main()