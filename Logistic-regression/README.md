# Logistic Regression
**Reference** [ https://en.wikipedia.org/wiki/Logistic_regression ]

## Background
This technique is associated with word regression, which essentially means to *model a best-fit line* across the feature points. In logistic regression, we take one or more predictor and give outcome(or class) as *binary categorical value*, which refers to values as true/ false, or 0/1.

The specific requirememnt of outcome as categorical value made to use a probabilistic model, which can work like *a step function*. Following this, a similar function called *sigmoid* to be used here as a smoothening step funtion.

Sigmoid is balanced a 0, sigmoid reaches to 1 as we increase the value, and touches 0 as we decrease the value from 0. Hence it is very *easy to classify*, for sigmoid function value of *>0.5 will classify as 1*, else 0 otherwise.

Now for giving input to sigmoid funtion, we need *an optimization algorithm*, that will give best fit points for the designated training vector. Here we use *Gradient Ascent* for finding out the weights for the training data, and update it as we move forward to our target.

**Note:-** 
*Stochastic gradient ascent algorithm* must be applied for better optimization in terms of doing matrics multiplication. 

## Run in Python interactive shell
    >>> import logRegres

    >>> dataArr,labelMat=logRegres.loadDataSet()

    >>> weights = logRegres.gradAscent(dataArr,labelMat)

    >>> logRegres.plotBestFit(weights)

## Referencs
Brahim Chaibdraa 
<chaib@iad.ift.ulaval.ca>
