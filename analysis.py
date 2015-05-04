import csv
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

def analyze(run_data):
	with open(run_data, 'r') as f:
		data = csv.reader(f)
		lines = list(data)
	mse_sum = 0
	diff_max = 0
	exp_vec = []
	est_vec = []
	diff_vec = []
	for row in lines:
		exp_vec.append(float(row[0]))
		est_vec.append(float(row[1]))
		diff = float(row[1])-float(row[0])
		diff_max = max(diff_max, abs(diff))
		diff_vec.append(diff)
		mse_sum += math.pow(diff, 2)
	rmse = math.sqrt(mse_sum/float(len(lines)))

	#Bin differences by frequency
	#Bin size is half the RMSE
	#How many
	num_bins = int(math.ceil(diff_max/(rmse/2)))
	bins = [x*(rmse/2) for x in xrange(-1*num_bins, num_bins)]
	freq_vec = []
	for i in xrange(0, len(bins)-1):
		freq = 0
		for e in diff_vec:
			if bins[i] <= e < bins[i+1]:
				freq += 1
		freq_vec.append(freq)

	#Do plotting
	plt.figure(1)
	plt.plot(bins[0:len(bins)-1], freq_vec)
	ax = plt.axes()
	ax.xaxis.grid()
	plt.xticks([round(x, 1) for x in bins[0:len(bins)]], [str(0.5*x) for x in range(-num_bins, num_bins)])
	plt.axvline(x=0.0, color='r')
	plt.xlabel('Difference Between Estimation and Actual\n(Bin Size RMSE)')
	plt.ylabel('Frequency')
	plt.title('Difference vs. Frequency\nUsing '+sys.argv[2]+' Method')

	plt.figure(2)
	plt.xlabel('Estimated MMSE Score')
	plt.ylabel('Actual MMSE Score')
	plt.minorticks_on()
	plt.grid(b=True, which='minor')
	plt.scatter(est_vec, exp_vec)
	plt.title('Estimated vs. Actual\nUsing '+sys.argv[2]+' Method')
	plt.text(0.7, 0.05, 'R = '+str(round(pearsonr(est_vec, exp_vec)[0], 5)), transform=plt.axes().transAxes, fontsize=15, color='red')
	plt.show()

analyze(sys.argv[1])