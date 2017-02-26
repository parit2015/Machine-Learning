from math import log

'''
Function to find out entropy
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}

    print "\n\nCreating a dict for label, count-" , "\n"
    for featVec in dataSet:

        currentLabel = featVec[-1]

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0

        labelCounts[currentLabel] += 1

        print "\t", featVec, " --> ", currentLabel, " --> count(",currentLabel,") = ", labelCounts[currentLabel]

    print "\n\n\tFinal dict for labelCounts is: ", labelCounts, "\n\n"

    print "Finding out the Entropy now, using following formula- \n"
    print "\t- ( Summation1-N { p(Xi).log_2( p(Xi) ) } )\n\n"
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        print "\tEntropy Summation = ", shannonEnt, "\n"
        print "\tFor (",key,") --> float(",labelCounts[key],") / ", numEntries ," = ", prob, " --> ", shannonEnt," - (", prob, "*log(", prob, ",2)) = "

        shannonEnt -= prob * log(prob,2)
        print "\t\t\t\t\t\t\t\t\t\t\t", shannonEnt, "\n"

    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]

    labels = ['no surfacing','flippers']

    return dataSet, labels
