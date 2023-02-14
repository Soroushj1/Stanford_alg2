

def max_weight_independent_set(input_arr,length):
    array = [0]
    array.append(input_arr[0])
    for i in range(1, length):
        array.append(max(array[i], array[i-1]+input_arr[i]))
    return array


def reconstruct(arr, input_arr):
    
    i = len(arr)-1
    independent_set = []
    while i >= 1:
        if arr[i-1] >= arr[i-2]+input_arr[i-1]:
            i-=1
        else:
            independent_set.append(i)
            i-=2
    return independent_set
    

def main():
    
    with open("MWIS.txt", "r", encoding="utf-8") as file: 
        input_arr = list(int(i) for i in file.read().strip().splitlines())
        length = input_arr.pop(0)
        mwis_arr = max_weight_independent_set(input_arr,length)
        independent_set = reconstruct(mwis_arr,input_arr)
        test_case = [1,2,3,4,17,117,517,997]
        empty_string = ""
        for i in test_case:
            if i in independent_set:
                empty_string+="1"
            else:
                empty_string+="0"
        print(empty_string)
        

if __name__ == "__main__":
    main()