#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
import pandas as pd
import numpy as np

def calcMissing(readings):
    
    data = pd.DataFrame(columns = ['time', 'value'])
    
    for line in readings:
        ts, val = line.strip().split('\t')
        data = data.append({'time':ts, 'value':val}, ignore_index=True)
    
    data['missing'] = 0    
    data.loc[data.value.str.contains("Missing"), 'missing'] = 1
    data.value[data.value.str.contains("Missing")] = np.nan

    data.value = data.value.astype(float)
    data.value = data.value.fillna(data.value.rolling(6,min_periods=1).mean())
    
    for j in data.value[data.missing == 1].values:
        print(np.round(j,2))


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
