#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrangingRules' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY rules as parameter.
#

import pandas as pd
import numpy as np

df = pd.read_csv('census.csv', header=None)
cols = []
for i in range(0, len(df.columns)):
    cols.append(df.iloc[0,i].split('=')[0])
    df.iloc[:, i] = [k[1] for k in df.iloc[:,i].str.split('=')]
df.columns = cols

nrows = df.shape[0]

def find_support(ls_rules):
    temp_df = df.copy()
    for l in ls_rules:
        column, value = l.split('=')
        temp_df = temp_df[temp_df[column] == value]
    return temp_df.shape[0]/nrows

def arrangingRules(rules):
    
    confidence_df = pd.DataFrame(columns=['Rule', 'Confidence'])
    for r in rules:
        a = r.split('=>')[0]
        b = r.split('=>')[1]

        a = re.sub('{', "", a)
        a = re.sub('}', "", a)
        b = re.sub('{', "", b)
        b = re.sub('}', "", b)

        ls_a = a.split(',')
        ls_b = b.split(',')

        support_a = find_support(ls_a)
        support_ab = find_support(ls_a + ls_b)

        confidence_atob = support_ab/support_a

        confidence_df = confidence_df.append({'Rule':r, 'Confidence':confidence_atob}, ignore_index = True)
    
    confidence_df = confidence_df.sort_values(by='Confidence', ascending = False)
    
    return list(confidence_df.Rule.values)
if __name__ == '__main__':
