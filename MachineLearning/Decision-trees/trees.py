from math import log

'''
Function to find out entropy for a given dataSet
'''
def calcShannonEnt(dataSet):
    #print "\n\tFinding out the Entropy now, using: - ( { p(Xi).log_2( p(Xi) ) } )\n"

    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0

        labelCounts[currentLabel] += 1
        #print "\t", featVec, " --> ", currentLabel, " --> count(",currentLabel,") = ", labelCounts[currentLabel]

    #print "\n\n\tDictionary created for p(Xi): ", labelCounts, "\n\n"
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        #print "\tFor (",key,") --> float(",labelCounts[key],") / ", numEntries ," = ", prob, " --> ", shannonEnt," - (", prob, "*log(", prob, ",2)) = "

        #print "\t", shannonEnt, "- [", prob, "*", log(prob,2), "]" 
        shannonEnt -= prob * log(prob,2)
        #print "\tEntropy: ", shannonEnt, "\n"

    #print "\tEntropy: ", shannonEnt, "\n"
    return shannonEnt

'''
Function to split the dataSet According to particular axis(i.e per feature), per unique-value wise
'''
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:

        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]

            reducedFeatVec.extend(featVec[axis+1:])
            #print "\t\t", featVec, " --> featVec[:",axis,"] = ",featVec[:axis], " --> ", featVec[:axis], ".extend(featVec[",axis,"+1:]) = ", reducedFeatVec 

            retDataSet.append(reducedFeatVec)
    
    #print "\n\t\tSplitted DataSet: ", retDataSet
    return retDataSet

'''
Splitting the dataset featurewise, and compare the corresponding shannon entropy.
Return the feature having highest infogain(i.e reduction in entropy)
'''
def chooseBestFeatureToSplit(dataSet):
    print "\n\n-> Choosing Best Feature to Split.\n"

    # Dataset contains features + class or label, so subtracting 1 
    numFeatures = len(dataSet[0]) - 1

    # Calculting base Entropy for comparision & updation everytime, if required
    print "\t--> Calculting the Base Entropy, <<<< using formula: - ( { p(Xi).log_2( p(Xi) ) } ) >>>>, (Without any splitting)"
    baseEntropy = calcShannonEnt(dataSet)
    print "\t--> Base entropy is: ", baseEntropy, "\n"

    # Setting the bestInfoGain and bestFeature
    bestInfoGain = 0.0; bestFeature = -1

    # For our sample, we have numFeatures as 2
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]

        uniqueVals = set(featList)
        #print "\t-> FeatureList for feature-", i, " = ", featList, " --> Set(", featList, ") = ", uniqueVals

        newEntropy = 0.0
        for value in uniqueVals:

            # Splitting the dataSet as according to per-axis-unique-value-wise
            subDataSet = splitDataSet(dataSet, i, value)
            print "\t\t--> SubDataSet after splitting across [ Axis(", i, "), value(", value,") ] = ", subDataSet, "\n"

            prob = len(subDataSet)/float(len(dataSet))

            print "\t\t--> Entropy for the just created subDataSet --> ", newEntropy, " + ", prob, " * ", calcShannonEnt(subDataSet), " = "
            newEntropy += prob * calcShannonEnt(subDataSet)
            print "\t\t\t\t\t\t\t\t\t\t\t\t",  newEntropy, "\n"
                                            
        #print "\n\n"
        print "\t--> Information Gain (For feature ", i, ") --> ", baseEntropy, " - ", newEntropy, " = ", baseEntropy - newEntropy, "\n"
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    
    print "\n\t*****************************************************************************************\n"
    print "\n\t--> Best feature till now = ", bestFeature, "with information gain as: ", bestInfoGain, "\n"
    print "\n\t*****************************************************************************************\n"
    return bestFeature

'''
Counting the majority count
'''
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
        
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
            
    return sortedClassCount[0][0]

'''
createTree function, will create a tree based on the tree-splitting decision 
'''
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
        
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
                                                              
    return myTree

'''
createDataSet function, creates a sample dataset.
'''
def createDataSet():
    features = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
           
    labels = ['no surfacing','flippers']
    
    return features, labels
