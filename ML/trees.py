from math import log

'''
Function to find out entropy for a given dataSet
'''
def calcShannonEnt(dataSet):

    print "\n\n\tFinding out the Entropy now, using following formula- \n"
    print "\t   - ( Summation1-N { p(Xi).log_2( p(Xi) ) } )\n\n"

    numEntries = len(dataSet)
    labelCounts = {}

    for featVec in dataSet:

        currentLabel = featVec[-1]

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0

        labelCounts[currentLabel] += 1

        print "\t", featVec, " --> ", currentLabel, " --> count(",currentLabel,") = ", labelCounts[currentLabel]

    print "\n\n\tDictionary created for p(Xi): ", labelCounts, "\n\n"

    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        print "\tFor (",key,") --> float(",labelCounts[key],") / ", numEntries ," = ", prob, " --> ", shannonEnt," - (", prob, "*log(", prob, ",2)) = "

        shannonEnt -= prob * log(prob,2)
        print "\t\t\t\t\t\t\t\t\t\t\t", shannonEnt, "\n"
    
    print "\n\n"
    return shannonEnt

'''
Function to split the dataSet According to particular axis(i.e per feature), per unique-value wise
'''
def splitDataSet(dataSet, axis, value):
    retDataSet = []

    print "\n\n"
    for featVec in dataSet:

        if featVec[axis] == value:

            reducedFeatVec = featVec[:axis]

            reducedFeatVec.extend(featVec[axis+1:])
            print "\t\t", featVec, " --> featVec[:",axis,"] = ",featVec[:axis], " --> ", featVec[:axis], ".extend(featVec[",axis,"+1:]) = ", reducedFeatVec 

            retDataSet.append(reducedFeatVec)
            print "\n\t\tSplitted DataSet: ", retDataSet, "\n\n"
            
    return retDataSet

'''
Splitting the dataset featurewise, and compare the corresponding shannon entropy.
Return the feature having highest infogain(i.e reduction in entropy)
'''
def chooseBestFeatureToSplit(dataSet):

    print "\n\n-> Choosing Best Feature to Split.\n\n"

    # Dataset contains features + class or label, so subtracting 1 
    numFeatures = len(dataSet[0]) - 1

    # Calculting base Entropy for comparision & updation everytime, if required
    print "\t-> Calculting the Base Entropy(Without any splitting) for comparision & updation everytime, (if required)"
    baseEntropy = calcShannonEnt(dataSet)
    print "\t-> Base entropy is: ", baseEntropy, "\n\n"

    # Setting the bestInfoGain and bestFeature
    bestInfoGain = 0.0; bestFeature = -1

    # For our sample, we have numFeatures as 2
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]

        uniqueVals = set(featList)
        print "\t-> FeatureList for feature-", i, " = ", featList, " --> Set(", featList, ") = ", uniqueVals

        newEntropy = 0.0
        
        for value in uniqueVals:

            print "\n\n"

            # Splitting the dataSet as according to per-axis-unique-value-wise
            print "\t-> Splitting dataSet(to get subDataSet) across [ Axis(", i, "), value(", value,") ]"
            subDataSet = splitDataSet(dataSet, i, value)

            prob = len(subDataSet)/float(len(dataSet))
            
            newEntropy += prob * calcShannonEnt(subDataSet)
            print "\t\t", subDataSet, "(SubDataSet) --> ", newEntropy, "(Entropy)"
                                            
        print "\n\n"
        print "\t-> Information Gain (For feature ", i, ") --> ", baseEntropy, " - ", newEntropy, " = ", baseEntropy - newEntropy 
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
            
        print "\n\n\t-> Best feature till now = ", bestFeature, "\n\n"

    return bestFeature


def createDataSet():
    dataSet = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
           
    labels = ['no surfacing','flippers']
    
    return dataSet, labels
