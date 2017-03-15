# naive-Bayes
**Reference** [ https://en.wikipedia.org/wiki/Naive_Bayes_classifier ]

# Background
Naive Bayes one of the *fastest probablistic classification* techniques, originated from Bayes theorem. This technique leverage the conditional probability with an assumptions/restrictions on the predictors(which are basically the features in Classification's lingo) being *conditionaly independent*.

It utilizes the conditional probability formula, where we caluculate the probability of getting a class, given the vector of word as part of training step.

              p(w|Ci) p(Ci)
    p(Ci|w) = -------------
                  p(w)
                  
    where,
        p(Ci|w) = Probability of getting class i, given the vector of words in our vocab
        p(Ci)   = Probability of getting class i
        p(w|Ci) = p(w0,w1,w2..wN|Ci) = p(w0|Ci) p(w1|Ci)....p(wN|Ci) Using the Naive assumption
       
Using the above formuala, probability of all the available class are calculated and compared to have a class as resultant prediction.

**Note:-** 
Naive Bayes 

## Run in Python interactive shell
    >>> 

    >>> 

    >>> 

## Referencs
Brahim Chaibdraa 
<chaib@iad.ift.ulaval.ca>
