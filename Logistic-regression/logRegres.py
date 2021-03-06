from numpy import *

'''
Parsing and loading the data
'''
def loadDataSet():

    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
        
    return dataMat,labelMat
        
'''
Sigmoid funtion, its a step funtion to be applied to get the classification
'''
def sigmoid(inX):
    
    return 1.0/(1+exp(-inX))
        
'''
Optimization algorithm "Gradient Ascent"-

1> Start with setting all weights to 1
2> Use sigmoid funtion to get the predicted class value
3> Compare the predicted class value with the actual class value
4> comparision get some error
5> Use that error to move in the error direction by the mentioned "steps", using our Gradient ascent optimization algorithm
6> Use step 5 to update the weight value

7> Repeat the steps 2 - 6 till you hit the target, or the maxCycle value
'''
def gradAscent(dataMatIn, classLabels):

    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()

    m,n = shape(dataMatrix)
    weights = ones((n,1))

    alpha = 0.001
    maxCycles = 500
    for k in range(maxCycles):

        h = sigmoid(dataMatrix*weights)

        # Taking the difference from actual and predicted class, so to move on in direction of the error
        error = (labelMat - h)

        ''' 
        > Calculation of weights repeatedly

           > gradient: z = w0x0 + w1x1 + ... + wnxn
                   i.e  wT.x
    
                where w = Best coefficient to move in the direction to
                      x = Input vector

           > Updated weights =  weights + alpha * gradient

        '''
        #gradient = error.transpose() * dataMatrix
        #print "\ngradient \n", gradient

        #weightDelta = alpha * gradient
        #print "\nweightDelta \n", weightDelta

        #weights = weights + weightDelta
        #print "\nUpdated weigths \n", weights

        weights = weights + alpha * dataMatrix.transpose() * error
        #print "\nUpdated weigths \n", weights

    return weights

'''
Function to generate the plot using pyplot
'''
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    
    weights = wei.getA()
    dataMat, labelMat=loadDataSet()
    dataArr = array(dataMat)
    
    n = shape(dataArr)[0]
    
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
            
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
            
    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
            
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
            
    ax.plot(x, y)
            
    plt.xlabel('X1'); plt.ylabel('X2');
            
    plt.show()
