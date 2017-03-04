from numpy import *

'''
Loading the dataset, in the form of different lists
'''
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
        
    # Class vector for the above dataset. 1 means abusive, 0 is non-abusive
    classVec = [0,1,0,1,0,1]

    '''
    So dataset can be represented as:-
        
                    Features                                                    class
                    ========                                                    =====

    [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],       ------> 0
    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],    ------> 1(abusive)
    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],       ------> 0
    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],             ------> 1(abusive)
    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'], ------> 0
    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]          ------> 1(abusive)
    '''
    
    return postingList, classVec
    
'''
Converting dataset into making distinct(no repeating features) single(witout multiple list) list
Which would be our vocab list now
'''
def createVocabList(dataSet):
    vocabSet = set([])
   
    # Taking each list from the dataset, and making it a distinct single list i.e set
    for document in dataSet:
        vocabSet = vocabSet | set(document)
        
    return list(vocabSet)
   
'''
Checking each word from input set, and try finding it up in vocablist,
once find the word, note down the index-number of the vocab list,
make that index number as 1.

And this would essencially be the training-matrics, to be use in training the classifier
'''
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
            
    for word in inputSet:
        if word in vocabList:

            # Making the returnVec list's index value = 1, where index number is same as vocablist index-number,
            # for which we found the match
            returnVec[vocabList.index(word)] = 1
            
        else: print "the word: %s is not in my Vocabulary!" % word
                    
    return returnVec

'''
Training the classifier,
Input:
trainMatrics - list of setOfWords2Vec vectors
trainCategory - list of classes

Output:
p0Vect -  Probability vector of being a non-abusive word, from vocablist, based on training dataset
p1Vect - Probability vector of being an abusive word, from vocablist, based on training dataset
pAbusive - Probability of being abusive
'''
def trainNB0(trainMatrix,trainCategory):

    print "\n\n"
    numTrainDocs = len(trainMatrix)
    print "\nNumber of trainMatrics, ", numTrainDocs

    numWords = len(trainMatrix[0])
    print "\nLength of Vocabulary(or features)", numWords

    pAbusive = sum(trainCategory)/float(numTrainDocs)
    print "\n=================================================================="
    print "pAbusive = sum(", trainCategory , ")/float(", numTrainDocs, ") = ", pAbusive
    print "=================================================================="

    # Changing the zeros to once, to avoid the multiplication to become zero
    #p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Num = ones(numWords); p1Num = ones(numWords)

    # Changing the denominators to 2.0, to avoid the above effect
    #p0Denom = 0.0; p1Denom = 0.0
    p0Denom = 2.0; p1Denom = 2.0

    print "\n\n"
    # i will range from 0-6, for this example.
    # means it will run for number of times as equal to number of training data available
    for i in range(numTrainDocs):
        print "\n\n" 
        # For class having value as 1, means it is symbolizing as abusive class
        # Updating the p1's- numerator & denominator
        if trainCategory[i] == 1:
            print "For category abusive- "
            print "\tp1Num = ", p1Num, " + ", trainMatrix[i]
            p1Num += trainMatrix[i]

            print "\tp1Denom = ", p1Denom, " + sum(", trainMatrix[i], ") "
            p1Denom += sum(trainMatrix[i])

            print "\n\n"
            print "\t==================================================================================="
            print "\tp1Num = ", p1Num, "\n\tp1Denom = ", p1Denom
            print "\t==================================================================================="

        # For non-Abusive class
        # Updating the p0's- numerator & denominator
        else:
            print "For category NoN-abusive- "
            print "\tp0Num = ", p0Num, " + ", trainMatrix[i]
            p0Num += trainMatrix[i]

            print "\tp0Denom = ", p0Denom, " + sum(", trainMatrix[i], ") "
            p0Denom += sum(trainMatrix[i])
    
            print "\n\n"
            print "\t==================================================================================="
            print "\tp0Num = ", p0Num, "\n\tp0Denom = ", p0Denom
            print "\t==================================================================================="

    print "\n\nAbusive vector"
    print "p1Vect = ", p1Num, " / ", p1Denom, " \n\n ", log(p1Num/p1Denom)

    # To avoid the underflow
    #p1Vect = p1Num/p1Denom      
    p1Vect = log(p1Num/p1Denom)

    print "\n\nNon-Abusive vector"
    print "p0Vect = ", p0Num, " / ", p0Denom, " \n\n ", log(p0Num/p0Denom)

    # To avoid the underflow
    #p0Vect = p0Num/p0Denom  
    p0Vect = log(p0Num/p0Denom)

    return p0Vect,p1Vect,pAbusive

'''
Classifier of NB
'''
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):

    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    
    if p1 > p0:
        return 1
        
    else:
        return 0

'''
Testcase for NB classifier
'''
def testingNB():
    
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    
    trainMat=[]
    for postinDoc in listOPosts:
        
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
        p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
        
        testEntry = ['love', 'my', 'dalmation']
        thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
        print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
        
        testEntry = ['stupid', 'garbage']
        thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
        print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
