import numpy as np

def linearRegressionWithMissingData(X,y):
    
    col_mean = np.nanmean(X, axis = 0)
    
    inds = np.where(np.isnan(X))
    X[inds] = np.take(col_mean, inds[1])
    
    b = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    yhat = X.dot(b)
    print(yhat)
    
    ybar = np.sum(y)/len(y)          
    ssreg = np.sum((yhat-ybar)**2)   
    sstot = np.sum((y - ybar)**2)
    print(ssreg, sstot)
    return sstot/ssreg
