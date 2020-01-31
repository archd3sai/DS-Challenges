# Importing Libraries
import numpy as np
import statistics as st
from scipy import stats

# Set data
n = int(input())
X = list(map(int, input().split()))

# Finding Statistics
mean = np.mean(X)
median = np.median(X)
mode = stats.mode(X)[0]
stdev = st.pstdev(X)
CI = [mean - 1.96*stdev/np.sqrt(n), mean + 1.96*stdev/np.sqrt(n)]

# Printing Values
print(round(mean, 1))
print(round(median, 1))
print(int(mode))
print(round(stdev, 1))
print(round(CI[0],1), round(CI[1],1))

