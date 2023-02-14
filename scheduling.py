

def read_file():
    with open("jobs.txt", "r", encoding="utf-8") as file:
        arr = list([int(j) for j in i.split(' ')] 
                   for i in file.read().strip().splitlines())
    
    return arr

def assign_score(arr):
    scores_diff= [] 
    scores_ratio = []
    for i in range(1, arr[0][0]+1):
        calc_diff = arr[i][0]- arr[i][1]
        calc_ratio = arr[i][0]/arr[i][1]
        scores_diff.append((calc_diff, arr[i][0], arr[i][1]))
        scores_ratio.append((calc_ratio, arr[i][0], arr[i][1]))
    new_scores_diff = sorted(scores_diff, reverse=True)
    new_scores_ratio = sorted(scores_ratio, reverse=True)
    
    return new_scores_diff, new_scores_ratio

def obj_func(scores):
    
    dist = 0 
    results = 0
    
    #rearrange if score is the same first based on higher weight
    i = 0
    while i < len(scores)-1:
        if scores[i][0] != scores[i+1][0]:
            i +=1
        else: 
            if scores[i][1] > scores[i+1][1]:
                i+=1
            else:
                scores[i+1], scores[i] = scores[i], scores[i+1]
                i+=1
                
    for elem in scores:
        dist += elem[2]
        results += elem[1]*dist
        
    return results
     
        
            
def main():
    arr = read_file()
    (scores_diff, scores_ratio) = assign_score(arr)
    schedule_diff = obj_func(scores_diff)
    schedule_ratio = obj_func(scores_ratio)
    
    print(schedule_diff, schedule_ratio)
    

if __name__ == "__main__":
    main()