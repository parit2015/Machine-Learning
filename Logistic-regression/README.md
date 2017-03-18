>>> import logRegres
>>> dataArr,labelMat=logRegres.loadDataSet()
>>> weights = logRegres.gradAscent(dataArr,labelMat)
>>> weights
matrix([[-3.77198489],
        [-0.03791254],
        [ 0.70466172]])
>>> logRegres.plotBestFit(weights)
