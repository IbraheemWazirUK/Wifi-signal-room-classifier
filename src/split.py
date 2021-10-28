from splitrule import SplitRule
import numpy as np

def find_split(training_dataset):
    (N, k) = training_dataset.shape
    return (SplitRule(0, N), np.array([]), training_dataset)
