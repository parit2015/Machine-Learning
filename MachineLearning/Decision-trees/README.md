# Decision trees
**Reference** [ https://en.wikipedia.org/wiki/Decision_tree ]

# Background
Being one of the *optimized classification* technique, decision tree *reduces the time complexity of visiting every data tuple*(that we found with kNN). Decision tree provides an optimized way of deriving the decision points and subsequently the classes/labels down lower in the tree.

Derivation of decision points is one of the importent and core process of this technique, it is also known as *splitting* across features in Decision tree lingo. *Information gain is calculated for every split* and compared to get the highest, to have the best split. This process of *splitting is repeated aross the remaining splitted dataset recursively*, till we reach to get the classes/labels in the created decision-tree.

Information gain is the *measure* of, how *easily we get the class/label(in an optimized fashion) of a new dataset-tuple*. Information gain is calculated using the *inverse relation of it with entropy*(or magnitude of disturbance or diversity), we are *using shannon entropy calculation formula* to caluculate the entropy in this technique.

Once we have the *best/highest Information gain*, we do a split across the corresponding feature(which is a decision point for traversing the tree). Running the same process recusively will give multiple decision points and *in turn tree creation will eventually hit the leaf nodes*(which are certainly be the classes/labels of the dataset)

The classification step for a new tuple is very simple, which actually requires to browse through the root to other intermediate nodes(i.e decision points, by reading the feature value as traversal path) to reach to leaf node, to get the class/label as a resultant.

**Note:-** Decision tree pruning

## Run in Python interactive shell
    >>> import trees

    >>> myDat, labels = trees.createDataSet()

    >>> myTree = trees.createTree(myDat, labels)    
    
    >>> myTree

## Referencs
Brahim Chaibdraa 
<chaib@iad.ift.ulaval.ca>
