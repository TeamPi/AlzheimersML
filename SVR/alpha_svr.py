#!/usr/local/bin/python
import sys
import csv
from sklearn import svm
from sklearn import grid_search

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

# open the training data and read into arrays
f = open(sys.argv[1], 'rt')
data_rows = csv.reader(f)
x_values = []
y_values = []
for i,row in enumerate(data_rows):
    if i == 0:
        continue
    for j,cell in enumerate(row):
        if j != 0:
            row[j] = float(cell)
    x_values.append(row[2:])
    y_values.append(row[1])

# assign alpha values
gamma_v = []
c_v = []
for i in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
    #for j in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
    gamma_v.append(i)
    c_v.append(3.45)
f.close()

# get the best alpha value using a grid seach on the model
model = svm.SVR()
grid = grid_search.GridSearchCV(estimator=svm.SVR(), param_grid=dict(C=c_v,gamma=gamma_v))
grid.fit(x_values,y_values)

best_lambda2 = grid.best_estimator_.gamma
print "Best Lambda2: " + str(best_lambda2)
