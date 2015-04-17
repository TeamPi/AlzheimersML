#!/usr/local/bin/python
import sys
import csv
from sklearn import linear_model

def main():
    f = open(sys.argv[1], 'rt')
    data_rows = csv.reader(f)

    x_values = [];
    y_values = [];
    for i,row in enumerate(data_rows):
        if i == 0:
            continue
        for j,cell in enumerate(row):
            if j != 0:
                row[j] = float(cell)
        x_values.append(row[2:])
        y_values.append(row[1])
    clf = linear_model.LinearRegression()
    clf.fit(x_values,y_values)
    print clf.coef_

    f.close()

main()
