import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function

    trainSet = StringIO(train_string)
    testSet = StringIO(test_string)

    # read in the training data and separate it to x_train and y_train
    trainingData= np.genfromtxt(trainSet)
    testData= np.genfromtxt(testSet)

    x_train=trainingData[:,:-1]
    y_train = np.asarray([])
    
    i=len(trainingData)-1
    while i>=0:
        last =trainingData[i][-1]
        y_train = np.insert(y_train,0,last,axis=0)
        i-=1
     
    # fit a linear regression model to the data and get the coefficients
    c = c=np.linalg.lstsq(x_train,y_train)[0]

    # read in the test data and separate x_test from it
    x_test = testData[:,:-1]

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
