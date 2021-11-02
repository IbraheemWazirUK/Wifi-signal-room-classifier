from datasets import clean_dataset
from cross_validation import get_cross_validation_metrics

avgs = get_cross_validation_metrics(clean_dataset)
print(avgs)
