# Logistic Regression
**Reference** [ https://en.wikipedia.org/wiki/Logistic_regression ]

## Background
This technique is associated with word regression, which essentially means to *model a best-fit line* across the feature points. In logistic regression, we take one or more predictor, and classify them to get *outcome(or class)* as *binary categorical values*, which refers to the values as true/ false, or 0/1.

The specific requirement of outcome as binary categorical value, made to use *a step function* as our probabilistic model. Here, we use *sigmoid* function, which is a smoothened step funtion.

> Sigmoid function is balanced at 0, sigmoid reaches to 1 as we increase the input value, and touches 0 as we decrease the value from 0. Hence it is very *easy to classify*, i.e for sigmoid function value of *>0.5 will be classified as 1*, else 0 otherwise.

Now for giving input to sigmoid funtion, we need *an optimization algorithm*, that gives best-fit points for the designated training vector. Here we use *Gradient Ascent* for finding out the weights for the training data, and update it as we move forward toward the target.

**Note:-** 
*Stochastic gradient ascent algorithm* must be applied for better optimization in terms of reducing number of matrics multiplication operations. 

## Run in Python interactive shell
    >>> import logRegres

    >>> dataArr,labelMat=logRegres.loadDataSet()

    >>> weights = logRegres.gradAscent(dataArr,labelMat)

    >>> logRegres.plotBestFit(weights)

## Referencs
Brahim Chaibdraa 
<chaib@iad.ift.ulaval.ca>
