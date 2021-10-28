from splitrule import SplitRule
def find_split(training_dataset):
    (N, k) = training_dataset.shape
    return SplitRule(0, N)


