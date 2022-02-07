import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    x_c=[]

    for coeff in c:
                 # edit here: calculate the sum of squared error with coefficient set coeff and
                 # keep track of the one yielding the smallest squared error
        x_c.append(X @ coeff)
    ## turn result into an np.array
    array=np.array(x_c)
    errors=[]

    ##use zip-function as in intermediate version
    for i in array:
        errors.append([(k-j)**2 for k, j in zip(y,i)])
    ## errors now has results for all version with 3 different set of coefficients
    ## lets check which is best

    smallest_error= sum(errors[0])
    for i in errors:
        if sum(i) <= smallest_error:
            best_index =errors.index(i)
            smallest_error=sum(i)




    print("the best set is set %d" % best_index)


find_best(X, y, c)
