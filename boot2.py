#!/usr/local/bin/python3

from random import random, seed, randrange

#create sample w replacement

def subsample(dataset, ratio=1.0):
	sample = []
	n_sample = round(len(dataset) * ratio)
	while len(sample) < n_sample:
		index = randrange(len(dataset))
		sample.append(dataset[index])
	return sample