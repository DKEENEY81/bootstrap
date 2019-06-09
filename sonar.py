#!/usr/local/bin/python3

import pandas as pd
import numpy as np

#import sonar data to df
dataset = pd.read_csv("sonar.all-data.csv", header=None)

#binarize Rock or Metal to 0,1 resp.
def binarize(df, col, val):
    df[col] = (df[col]==val).astype(int)
    return df

dataset = binarize(dataset, 60, "M")




