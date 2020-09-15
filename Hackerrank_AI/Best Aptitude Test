import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

testcases = int(input())

df = pd.DataFrame(columns = ['group', 'student', 'gpa', 'T1', 'T2', 'T3', 'T4', 'T5'])

for i in range(0, testcases):
    
    students = int(input())
    gpas = input().strip().split(' ')
    t1_marks = input().strip().split(' ')
    t2_marks = input().strip().split(' ')
    t3_marks = input().strip().split(' ')
    t4_marks = input().strip().split(' ')
    t5_marks = input().strip().split(' ')

    for j in range(0, students):
        df = df.append({'group' : i, 'student' : j, 'gpa' : gpas[j], 'T1' : t1_marks[j], 'T2' : t2_marks[j], 'T3' : t3_marks[j], 'T4' : t4_marks[j], 'T5' : t5_marks[j]}, ignore_index = True)

    scores_df = pd.DataFrame(columns = ['Test', 'Fit_val'])
    x_cols = df.columns.drop(['group', 'student', 'gpa'])

    for k in range(0, 5):
        X = df[x_cols[k]].values.reshape(df.shape[0],1)
        y = df.gpa.values.reshape(df.shape[0],1)
        lr = LinearRegression()
        lr.fit(X, y)

        scores_df = scores_df.append({'Test':k+1, 'Fit_val': lr.score(X, y)}, ignore_index = True)

    Best_Test = int(scores_df.Test[scores_df.Fit_val == scores_df.Fit_val.max()].values[0])
    print(Best_Test)    


