#!/usr/local/bin/python
from sklearn import linear_model

def main():
   clf = linear_model.Ridge (alpha = 0.5)
   print clf.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
   print clf.coef_
   print clf.intercept_

main()
