#!/usr/local/bin/python3
from random import randrange
from random import seed
from random import random
import numpy as np

#subsamples records w replacement from original data set

def subsample(dataset, ratio =1.0):
	sample = []
	n_sample = round(len(dataset) * ratio)
	while len(sample) < n_sample:
		index = randrange(len(dataset))
		sample.append(dataset[index])
	return sample

seed(2)
# actual mean
dataset = [[randrange(10)] for i in range(20)]
print('True Mean: %.3f' % np.mean(dataset))


# Estimated means
ratio = 0.20
for size in [1, 10, 100, 200, 1000, 2000, 5000]:
	sample_means = list()
	for i in range(size):
		sample = subsample(dataset, ratio)
		sample_mean = np.mean(sample)
		sample_means.append(sample_mean)
	print('Samples=%d, Estimated Mean: %.3f' % (size, np.mean(sample_means)))






