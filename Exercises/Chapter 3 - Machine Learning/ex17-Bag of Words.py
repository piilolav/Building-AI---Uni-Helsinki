import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    distance = []
    for i in range(len(row1)):
        distance.append(abs(row1[i]-row2[i]))
        i+=1
    total=0
    for ele in range(0, len(distance)):
        total = total + distance[ele]
    if total==0:
        total=np.inf
    return total

def find_nearest_pair(data):
    N = len(data)
    dist = np.inf
    dist = np.empty((N, N), dtype=np.float)

    for i in range(N):
        for j in range(N):
##            sum=0
##            for k in range(len(data[i])):
##                
##                sum += (data[j][k] - data[i][k])
##                dist[i][j] = sum
                dist[i][j]=distance(data[i],data[j])
    
    
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
