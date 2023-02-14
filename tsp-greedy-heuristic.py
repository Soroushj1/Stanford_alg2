
import numpy as np
from math import sqrt

def distance_calc (city_a, city_b):
    return sqrt((city_a[0]-city_b[0])**2 + (city_a[1]-city_b[1])**2)




def tsp(cities, start, size):
    
    inf = np.inf
    traveled_set = set()
    traveled_set.add(start)

    next = start
    next_pos = cities[start]
    distance = 0 
    while len(traveled_set) < size:
        
        min_dist = inf
        
        for city in cities:
            if city not in traveled_set:
                dist = distance_calc(next_pos, cities[city])
                if not dist > min_dist:
                    if dist < min_dist:
                        min_dist = dist
                        min_city = city
                    else:
                        if city < min_city:
                            min_dist = dist
                            min_city = city
        
        next = min_city
        next_pos=cities[next]
        cities.pop(next)
        traveled_set.add(next)
        distance += min_dist
    
    distance += distance_calc(next_pos, cities[start])
    return distance
        
                    
                    
            

def cities_pos(file):
    
    with open(file, "r", encoding="utf-8") as file:
        arr = [[float(j) for j in dist.split(" ")]for i, dist in enumerate(file.read().strip().splitlines())]
        size = int(arr[0][0])
        arr = arr[1:]
        
        cities = {}
        for i in range(size):
            cities[int(arr[i][0])] = (arr[i][1], arr[i][2])
    
    return cities, size


def main():
    
    start = 1
    cities, size = cities_pos("tsp-greedy-heuristic.txt")
    distance = tsp(cities, start,size)
    print(distance)


if __name__ == "__main__":
    main()