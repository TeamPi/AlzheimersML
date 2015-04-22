import csv
import sys
import math

def main():
	with open(sys.argv[1], 'r') as f:
		data = csv.reader(f)
		lines = list(data)
	length = float(0)
	mse_sum = 0
	for row in lines:
		length += 1
		mse_sum += math.pow(float(row[0])-float(row[1]), 2)
	rmse = math.sqrt(mse_sum/length)
	print 'Standard deviation: '+str(rmse)
	#How many are within 1 standard deviation?
	count = 0
	for row in lines:
		if abs(float(row[0])-float(row[1])) <= rmse:
			count += 1
	print 'Percentage of estimates within 1 standard deviation: '+str((count/length)*100)+'%'
	#How many are within 2 standard deviations?
	count = 0
	for row in lines:
		if abs(float(row[0])-float(row[1])) <= 2*rmse:
			count += 1
	print 'Percentage of estimates within 2 standard deviations: '+str((count/length)*100)+'%'

main()