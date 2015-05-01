import csv
import sys
import math
import matplotlib.pyplot as plt
import pprint

def analyze(run_data):
	with open(run_data, 'r') as f:
		data = csv.reader(f)
		lines = list(data)
	length = float(0)
	mse_sum = 0
	diff_max = 0
	diff_vec = []
	for row in lines:
		length += 1
		diff = float(row[1])-float(row[0])
		diff_max = max(diff_max, abs(diff))
		diff_vec.append(diff)
		mse_sum += math.pow(diff, 2)
	rmse = math.sqrt(mse_sum/length)

	#Bin differences by frequency
	#Bin size is half the RMSE
	#How many
	num_bins = int(math.ceil(diff_max/(rmse/2)))
	bins = [x*(rmse/2) for x in range(-1*num_bins, num_bins)]
	freq_vec = []
	for i in xrange(0, len(bins)-1):
		freq = 0
		for e in diff_vec:
			if bins[i] <= e < bins[i+1]:
				freq += 1
		freq_vec.append(freq)

	#pprint.pprint(freq_vec)
	#pprint.pprint(bins)

	#Do plotting
	plt.plot(bins[0:len(bins)-1], freq_vec)
	plt.xticks(bins[0:len(bins)-1])
	plt.show()


analyze(sys.argv[1])