from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']

    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    print "1) Converting the input-data instance into matrics form. By creating a tile of (inX, [Size of Axis-0 of dataset, 1]): \n\n", tile(inX, (dataSetSize,1)), "\n\n"

    print "2) Applying euclidian distance algo to find out distance between input-data instance and provided dataset, using the formula\n\td = squareRoot((inX_0 - dataSet_0)^2  +
 (inX_1 - dataSet_1)^2)).\n"
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print "\t", "=== Taking difference from dataset ==> \n\n", diffMat, "\n\n"

    sqDiffMat = diffMat**2
    print "\t", "============ Squaring up ============> \n\n", sqDiffMat, "\n\n"

    sqDistances = sqDiffMat.sum(axis=1)
    print "\t", "======= Summing up across axis-1 ====> \n\n", sqDistances, "\n\n"

    distances = sqDistances**0.5
    print "\t", "========== Taking SquareRoot ========> \n\n", distances, "\n\n\n"

    sortedDistIndicies = distances.argsort()
    print "3) Find out the nearest k distances.\n\n"
    print "\t * Value of sortedDistIndicies: \n\n", sortedDistIndicies, "\n\n"

    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]

        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "\t * SortedClassCount is: \n\n", sortedClassCount, "\n\n"

    print "4) Returning the following value: \n\n", sortedClassCount[0][0], "\n\n"
    return sortedClassCount[0][0]
