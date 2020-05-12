import numpy as np
import random

## TODO: Implement this function
##
## Input:
##  - dmat (np.array): symmetric array of distances
##  - K (int): Number of clusters
##
## Output:
##   (np.array): initialize by choosing random number of points as medioids
def random_init(dmat, K):
    num_vertices = dmat.shape[0]
    medioids = random.sample(range(0,num_vertices),2)
    return medioids

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - medioids (np.array): indices of current medioids
##
## Output:
##   - (np.array): assignment of each point to nearest medioid
def assign(dmat, mediods):
    num_vertices = dmat.shape[0]
    assignment = [0] * num_vertices 
    
    med1 = dmat[mediods[0],:]
    med2 = dmat[mediods[1],:]
    
    for i in range(num_vertices):
        if med1[i] <= med2[i]:
            assignment[i] = 1
        else:
            pass
        
        
    return assignment

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - assignment (np.array): cluster assignment for each point
##   - K (int): number of clusters
##
## Output:
##   (np.array): indices of selected medioids
def get_medioids(dmat, assignmentt, K):
    num_vertices = dmat.shape[0]
    mediods = np.zeros((K))
    assignmentg = [0] * num_vertices
    for i in range(num_vertices):
        
        for j in range(num_vertices):
            
            assignmentg = [0] * num_vertices 
            medg1 = dmat[i,:]
            medg2 = dmat[j,:]
            for k in range(num_vertices):
                if medg1[k] <= medg2[k]:
                    assignmentg[k] = 1
                else:
                    pass   
                v = assignmentt == assignmentg
               
                val=v.all()
                if val == True:
                    mediods = [i,j]
                    break
    
    return mediods

## TODO: Finish implementing this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - K (int): number of clusters
##   - niter (int): maximum number of iterations
##
## Output:
##   - (np.array): assignment of each point to cluster
def kmedioids(dmat, K, niter=10):
    num_vertices = dmat.shape[0]
    
    # we're checking for convergence by seeing if medioids
    # don't change so set some value to compare to
    old_mediods = np.full((K), np.inf, dtype=np.int)
    mediods = random_init(dmat, K)
    
    # this is here to define the variable before the loop
    assignment = np.full((num_vertices), np.inf)
   
    it = 0
    while np.any(old_mediods != mediods) and it < niter:
        it += 1
        old_medioids = mediods
        
        # finish implementing this section
        
        assignment = assign(dmat,mediods)
        mediods = get_medioids(dmat, assignment, mediods)

    return assignment
        