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
alphat_v = []
lamb_v = []
lambt_v = []
for i in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
   # for j in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
    #    for k in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
     #       for l in frange(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])):
    alpha_v.append(-51.5)
    alphat_v.append(-.0000000001)
    lamb_v.append(-5)
    lambt_v.append(i)
f.close()

# get the best alpha value using a grid seach on the model
model = linear_model.BayesianRidge()
grid = grid_search.GridSearchCV(estimator=linear_model.BayesianRidge(), param_grid=dict(alpha_1=alpha_v, alpha_2=alphat_v, lambda_1=lamb_v,lambda_2=lambt_v))
grid.fit(x_values,y_values)
# print out and store the best alpha value
#best_alpha1 = grid.best_estimator_.alpha_1
#best_alpha2 = grid.best_estimator_.alpha_2
#best_lambda1 = grid.best_estimator_.lambda_1
best_lambda2 = grid.best_estimator_.lambda_2
#print "Best Alpha1: " + str(best_alpha1)
#print "Best Alpha2: " + str(best_alpha2)
#print "Best Lambda1: " + str(best_lambda1)
print "Best Lambda2: " + str(best_lambda2)
