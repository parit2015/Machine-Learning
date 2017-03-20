# naive-Bayes
**Reference** [ https://en.wikipedia.org/wiki/Naive_Bayes_classifier ]

# Background
Naive Bayes is one of the *fastest probablistic classification* techniques, originated from Bayes theorem. This technique leverages the conditional probability formula with an assumptions on the predictors(i.e features) being *conditionaly independent*.

It utilizes the conditional probability formula, where we calculate the probability of getting a class, given the vector of word as part of training step.

              p(w|Ci) p(Ci)
    p(Ci|w) = -------------
                  p(w)
                  
    where,
        p(Ci|w) = Probability of getting class i, given the vector of words in our vocab
        p(Ci)   = Probability of getting class i
        p(w|Ci) = p(w0,w1,w2..wN|Ci) = p(w0|Ci) p(w1|Ci)....p(wN|Ci) Using the Naive assumption
       
Using the above formula, probability of all the available classes are calculated and compared to have a single class(with having highest probability) as resultant prediction.

## Run in Python interactive shell
    >>>import bayes
    
    >>>bayes.testingNB() 

## Referencs
Brahim Chaibdraa 
<chaib@iad.ift.ulaval.ca>
