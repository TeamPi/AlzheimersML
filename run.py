import sys
import time

from analysis import analyze
sys.path.insert(0, './ridge')
from ridge import ridge
sys.path.insert(0, './lasso')
from lasso import lasso
sys.path.insert(0, './bayesian')
from bayesian import bayesian
sys.path.insert(0, './SVR')
from svr import svr

start = time.time()
ridge(sys.argv[1],sys.argv[2])
ridge_end = time.time()
lasso(sys.argv[1],sys.argv[2])
lasso_end = time.time()
bayesian(sys.argv[1],sys.argv[2])
bayesian_end = time.time()
svr(sys.argv[1],sys.argv[2])
svr_end = time.time()

print "Ridge Results"
print "Running Time: "+str(ridge_end-start)+" seconds"
analyze("ridge_out.csv")
print "---"
print "Lasso Results"
print "Running Time: "+str(lasso_end-ridge_end)+" seconds"
analyze("lasso_out.csv")
print "---"
print "Bayesian Results"
print "Running Time: "+str(bayesian_end-lasso_end)+" seconds"
analyze("bayesian_out.csv")
print "---"
print "SVR Results"
print "Running Time: "+str(svr_end-bayesian_end)+" seconds"
analyze("svr_out.csv")
