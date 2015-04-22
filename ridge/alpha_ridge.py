#!/usr/local/bin/python
import sys
import csv
from sklearn import linear_model
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
alpha_v = []
for i in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
    alpha_v.append(i)
f.close()

# get the best alpha value using a grid seach on the model
model = linear_model.Ridge()
grid = grid_search.GridSearchCV(estimator=linear_model.Ridge(), param_grid=dict(alpha=alpha_v))
grid.fit(x_values,y_values)
# print out and store the best alpha value
best_alpha = grid.best_estimator_.alpha
print "Best Alpha: " + str(best_alpha)
