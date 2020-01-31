# Importing Libraries
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Set data
features, rows = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = []
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set Polynomial Features
poly = PolynomialFeatures(degree=3)

# Set the model LinearRegression
model = LinearRegression()
model.fit(poly.fit_transform(np.array(X)), Y)

# Get the parameters X for discovery the Y
new_rows = int(input())
new_X = []
for i in range(new_rows):
    x = []
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = model.predict(poly.fit_transform(np.array(new_X)))
for i in range(len(result)):
    print(round(result[i],2))
