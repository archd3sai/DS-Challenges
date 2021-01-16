# IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
# SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
# DEFINE ANY CLASS AND METHOD NEEDED
# THIS FUNCTION IS REQUIRED
#
# Parameters:  y: ndarray, shape (n_samples,1)
# 	       y_pred: ndarray, shape (n_samples,1)
#              Thres: list
#              
# Returns:     score: list
#	

import numpy as np

def computePrecisionRecall(y,y_pred,Thres):
# INSERT YOUR CODE HERE
    op = []
    y = y.reshape(y.shape[0],)

    j = 0
    for t in Thres:
        preds = [1 if i > t else 0 for i in y_pred]

        tp = 0.0
        fp = 0.0
        fn = 0.0
        for i, p in enumerate(preds):
            if p == 1:
                if y[i] == 1:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if y[i] == 1:
                    fn = fn + 1
        
        pr = round(tp / (tp + fp),2)
        re = round(tp / (tp + fn),2)
        op.append([pr, re])
            
    return np.array(op).T 
    
computePrecisionRecall(np.array([1,0,1,0,1,1]), np.array([0.6, 0.5, 0.7,.3,.8,.9]), np.array([0.55,0.65, 0.6]))
