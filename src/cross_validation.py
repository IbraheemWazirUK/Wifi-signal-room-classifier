from k_folds import create_k_models
from evaluator import get_evaluation_metrics
from dtl import decision_tree_learning
from pruning import prune, get_validation_error
from utils import add_parents, get_tree_depth
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
    print("Label to index map: " + str(labels))
    return labels


def get_cross_validation_metrics(
    dataset, pruning=False, k=10, rng=np.random.default_rng()
):
    labels = get_labels(dataset)
    n = len(labels)
    testing_models = create_k_models(dataset, k, rng)
    sum_confusion_matrix = np.zeros((n, n))
    sum_accuracy = 0
    sum_precision = 0
    sum_recall = 0
    sum_f1 = 0
    depth_total = 0
    # outer cross validation
    for (test_db, training_and_validation_db) in testing_models:
        validation_models = create_k_models(training_and_validation_db, k, rng)
        min_validation_error = 1
        best_trained_tree = None
  #      for row in test_db:
 #           if row in training_and_validation_db:
#                print("ALERT")
        # inner cross validation
        for (validation_db, training_db) in validation_models:
            (trained_tree, depth) = decision_tree_learning(training_db, 0)
            if pruning:
                cur_tree = trained_tree
                add_parents(cur_tree, None)
                cur_tree = trained_tree
                prune(cur_tree, validation_db, trained_tree)
            validation_error = get_validation_error(validation_db, trained_tree)
            if validation_error <= min_validation_error:
                best_trained_tree = trained_tree
                min_validation_error = validation_error
        depth_total += get_tree_depth(best_trained_tree, 0)
        (cm, acc, p, r, f1) = get_evaluation_metrics(test_db, best_trained_tree, labels)
        sum_confusion_matrix += cm
        sum_accuracy += acc
        sum_precision += p
        sum_recall += r
        sum_f1 += f1
    depth = depth_total / k
    print(f"Average Tree Depth: {depth}")
    sums = [sum_confusion_matrix, sum_accuracy, sum_precision, sum_recall, sum_f1]
    avgs = [s / k for s in sums]
    return avgs
