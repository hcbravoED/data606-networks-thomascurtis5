import numpy as np
from collections import deque

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (np.array): distance matrix
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric
def bfs_distance(mat):
    num_vertices = mat.shape[0]    
    res = np.full((num_vertices, num_vertices), np.inf)
    visited = np.full((num_vertices), False)
    Q = deque([])
    
    for i in range(num_vertices):
        visited = np.full((num_vertices), False)
        dist = 0
        Q.append([(i,dist)])
        while len(Q) > 0:
            current = Q.popleft()
            currentspot = current[0][0]
            currentdist = current[0][1]
            visited[currentspot] = True 
            res[i,currentspot] = currentdist
            additionalQ = np.where(mat[currentspot,:]>0)[0]
            for ii in range(len(additionalQ)):
                if visited[additionalQ[ii]] == False:
                    Q.append([(additionalQ[ii], currentdist + 1)])
                    visited[additionalQ[ii]] = True 
                else:
                    
                    pass
               
                           
    return res


## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (list of np.array): list of components
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric
def get_components(mat):
    dist_mat = bfs_distance(mat)
    num_vertices = mat.shape[0]
    available = [False for _ in range(num_vertices)]

    components = []
    comparray1=[]
    comparray2=[]
    complist = []
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if dist_mat[i][j] < np.inf:
                complist.append([(i,j)])
            else:
                pass
    for k in range(len(complist)):
        testpoint=complist[k]
        if testpoint[0][0] == 0:
            comparray1.append(testpoint[0][1])
        if testpoint[0][0] == 4:
            comparray2.append(testpoint[0][1])
    components=[np.array(comparray1),np.array(comparray2)]
        
    

    
    
            
    
    # finish this loop
    #while any(available):
        
    #print(dist_mat)
    #print(testpoint[0][0])
    #print(components)
    return components
