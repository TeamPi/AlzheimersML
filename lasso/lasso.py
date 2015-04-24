#!/usr/local/bin/python
import sys
import csv
from sklearn import linear_model
from sklearn import grid_search

fname = "lasso"
# call this file as follows:
#   python lasso.py train_data.csv test_data.csv alpha_value
# optimal alpha value for lasso = .1868
# this alpha value can be generated by using the alpha_lasso.py script

def main():
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
    
    # assign alpha value
    best_alpha = 0.1868
    
    # fit the training data to the ridge model with the alpha value
    clf = linear_model.Lasso(alpha=best_alpha)
    clf.fit(x_values,y_values)
    
    # open the test data and read into arrays
    f = open(sys.argv[2], 'rt')
    data_rows = csv.reader(f)
    x_values = []
    y_values = []
    for i,row in enumerate(data_rows):
        if i == 0:
            continue
        for j, cell in enumerate(row):
            if j != 0:
                row[j] = float(cell)
        x_values.append(row[2:])
        y_values.append(row[1])
    
    # use the regression model to estimate targets
    results = clf.predict(x_values)
    
    # write the actual values and estimates to file
    f = open(fname+"_out.csv", 'w')
    fwrite = csv.writer(f, delimiter=',')
    for i,row in enumerate(results):
        fwrite.writerow([y_values[i],row])
    f.close()

main()
   	#print clf.score(x_values,y_values)
   	#diffs = []
   	#avg_diff = 0.0
   	#for i,v in enumerate(results):
   	#    results[i] = int(v)
   	#    diff = abs(results[i] - y_values[i])
   	#    diffs.append(diff)
   	#    avg_diff += float(diffs[i])/len(results)
