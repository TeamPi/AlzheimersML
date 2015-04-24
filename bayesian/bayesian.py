#!/usr/local/bin/python
import sys
import csv
from sklearn import linear_model

fname = "bayesian"

def main():
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
    clf =  linear_model.BayesianRidge(alpha_1=-51.5, alpha_2=-1e-10, lambda_1=-5,lambda_2=-.03)
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
    f.close()
    results = clf.predict(x_values)

    f = open(fname+"_out.csv", 'w')
    fwrite = csv.writer(f, delimiter=',')
    for i,row in enumerate(results):
        fwrite.writerow([y_values[i],row])
    f.close()

main()
