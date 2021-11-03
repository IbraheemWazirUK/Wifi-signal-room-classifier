from datasets import noisy_dataset
from cross_validation import get_cross_validation_metrics

avgs = get_cross_validation_metrics(noisy_dataset, pruning=True)
print(avgs)
