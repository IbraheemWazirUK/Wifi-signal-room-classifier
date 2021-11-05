from datasets import clean_dataset, noisy_dataset
from cross_validation import get_cross_validation_metrics


def print_metrics(metrics):
    print("Confusion matrix:\n ", metrics[0])
    print("Accuracy: ", metrics[1])
    print("Precision: ", metrics[2])
    print("Recall: ", metrics[3])
    print("F1-Measure: ", metrics[4])


print("Clean dataset validation metrics")
avgs = get_cross_validation_metrics(clean_dataset)
print_metrics(avgs)
print("\n Noisy dataset validation metrics")
avgs = get_cross_validation_metrics(noisy_dataset)
print_metrics(avgs)
print("\n Clean dataset validation metrics after pruning")
avgs = get_cross_validation_metrics(clean_dataset, pruning=True)
print_metrics(avgs)
print("\n Noisy dataset validation metrics after pruning")
avgs = get_cross_validation_metrics(noisy_dataset, pruning=True)
print_metrics(avgs)
