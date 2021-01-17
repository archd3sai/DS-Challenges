import numpy as np

# Actual Values
a = [1,0,1,0,1,0,1,0] 

# Predicted Values
b = [1,1,1,1,0,0,1,0] 

result = np.zeros((2, 2))

for i in range(len(a)):
    result[a[i]][b[i]] += 1

print(result)  

#          Predicted
#           0     1    
# Actual 0 [TN   FP]
#        1 [FN   TP]

TP = result[1,1]
FP = result[0,1]
TN = result[0,0]
FP = result[1,0]

Precision = TP / (TP + FP) 
Precision = result[1,1]/ np.sum(result[:,1])

Recall = TP / (TP + FN)
Recall = result[1,1]/ np.sum(result[1,:])

F1 = 2*Precision*Recall/(Precision + Recall)

