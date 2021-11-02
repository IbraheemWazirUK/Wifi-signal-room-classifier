from k_folds import create_k_models
from evaluator import get_evaluation_metrics
from dtl import decision_tree_learning
import numpy as np
def get_labels(dataset):
    (N, k) = dataset.shape
    labels = {}
    label_count = 0
    for i in range(N):
        label = dataset[i, -1]
        if not (label in labels):
            labels[label] = label_count
            label_count += 1
    return labels

    
def get_cross_validation_metrics(dataset, k=10, rng=np.random.default_rng()):
    labels = get_labels(dataset)
    n = len(labels)
    models = create_k_models(dataset, k, rng)
    sum_confusion_matrix = np.zeros((n, n))
    sum_accuracy = 0
    sum_precision = 0
    sum_recall = 0
    sum_f1 = 0 
    for (test_db, training_db) in models:
        (trained_tree, _) = decision_tree_learning(training_db, 0)
        (cm, acc, p, r, f1) = get_evaluation_metrics(test_db, trained_tree, labels)
        sum_confusion_matrix += cm
        sum_accuracy += acc
        sum_precision += p
        sum_recall += r
        sum_f1 += f1

    sums = [sum_confusion_matrix, sum_accuracy, sum_precision, sum_recall, sum_f1]
    avgs = [s/k for s in sums]
    return avgs

