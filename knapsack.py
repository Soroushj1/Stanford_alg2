
def knapsack(arr, cap, num):
    # sack = list([None for j in range(cap)] for i in range(num))
    sack = []
    for i in range(num+1):
        items = []
        for x in range(cap+1):
            if i ==0:
                items.append(0)
            elif x < arr[i-1][1]:
                value = sack[i-1][x]
                items.append(value)
            else:
                value= max(sack[i-1][x], sack[i-1][x-arr[i-1][1]]+arr[i-1][0])
                items.append(value)
        sack.append(items)
    return sack

def reconstruct():
    # didn't implement it. But it should be straightforward 
    # and its backtracing the decision we are making in the max argument above
    pass


def main():
    
    with open("knapsack.txt", "r", encoding="utf-8") as file:
        arr = list([int(j)for j in i.split(" ")]for i in file.read().strip().splitlines())
        cap = arr[0][0]
        num= arr[0][1]
        optimal = knapsack(arr[1:],cap, num)
        print(optimal[-1][-1])
        

if __name__ == "__main__":
    main()