# Decision trees
**Reference** [ https://en.wikipedia.org/wiki/Decision_tree ]

# Background
Being one of the optimized classification technique, decision tree reduces the time complexity of visiting every data-tuple(that we found with kNN). Decision tree provides an optimized way of deriving the decision points and subsequently the classes/labels down lower in the tree.

Derivation of decision points is one of the importent and core process of this technique, it is also known as splitting across  features in Decision tree lingo. 

**Note:-** 

## Run in Python interactive shell
    >>> import trees

    >>> myDat, labels = trees.createDataSet()

    >>> myTree = trees.createTree(myDat, labels)    
    
    >>> myTree

## Referencs
Brahim Chaibdraa 
<chaib@iad.ift.ulaval.ca>
