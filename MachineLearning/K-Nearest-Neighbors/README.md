# k-Nearest Neighbors
**Reference** [ https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm ]

# Background
kNN belongs to one of the *classification techniques* in supervised learning. 

This technique *doesn't need any separate training step* rather it takes training data in the form of existing dataset. Dataset *contains feature and its associated class/label*. 

We represent the features as a points on the respective plane. Everytime once we want to predict the class of new incoming data, we do a *distance calculation from the existing data-points*, and choose the nearest neighbours.

The distance is calculated based on the *euclidean distance calculation formula*(which basically follows the pythagorean axiom), and gives us the distance value. Once after getting the distance value, we choose upon the *best k values*. These k values actually helps in narrowing down our process of selection. Among these values, we choose the one, which is having *highest votes*(in terms of class/label associated with it) in the group, and declear it a winner.

Our predication process will stop here, and results the class/label of the winning neighbour as the class/label of the incoming data.

kNN is subjected to be working good with *small to medium range of the dataset*, large dataset consumes more time in browsing through all the datapoints present in the dataset.

**Note:-** Care should be taken at the time of taking distances between the points, sometime one of the *feature can dominate over the others*(because of having large values). *Normalization of dataset is recommanded* before starting up the process.

## Run in Python interactive shell
    >>> import kNN

    >>> dataSet, labels = kNN.createDataSet()

    >>> kNN.classify0([0,0], dataSet, labels, 3)    # where k = 3, and inX = [0,0]

