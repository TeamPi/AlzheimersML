# lasso regression

import sys
import csv
from sklearn import linear_model
import warnings

def main():
	
	warnings.simplefilter("always")
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
   	alpha_v = []
   	for i in range(1,10):
   	    alpha_v.append(float(i))
   	clf = linear_model.LassoCV(alphas=[0.1, 1, .001, 10], max_iter=10000)
   	clf.fit(x_values,y_values)
   	f.close()

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
   	results = clf.predict(x_values)
   	print clf.score(x_values,y_values)
   	diffs = []
   	avg_diff = 0.0
   	for i,v in enumerate(results):
   	    results[i] = int(v)
   	    diff = abs(results[i] - y_values[i])
   	    diffs.append(diff)
   	    avg_diff += float(diffs[i])/len(results)
   	f.close()

main()