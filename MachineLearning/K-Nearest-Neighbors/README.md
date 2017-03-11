# k-Nearest Neighbors
**Reference** [ https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm ]

# Background
kNN belongs to one of the classification techniques in supervised learning. This algorithm doesnot need any separate training step rahter it takes training data in the form of existing dataset. Since this lies under classification, dataset contains feature and respective class associated with every individual data.



## Run in Python interactive shell
    >>> import kNN

    >>> dataSet, labels = kNN.createDataSet()

    >>> kNN.classify0([0,0], dataSet, labels, 3)    # where k = 3, and inX = [0,0]

