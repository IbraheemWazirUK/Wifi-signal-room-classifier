from classifier import classify
import numpy as np

def get_evaluation_metrics(test_db, trained_tree, labels):
    (N, k) = test_db.shape
    correct_count = 0
    n = len(labels)
    confusion_matrix = np.zeros((n, n), dtype=int)
    true_positive = np.zeros(n)
    false_negative = np.zeros(n)
    false_positive = np.zeros(n)
    for i in range(N):
        predicted_label = classify(test_db[i], trained_tree)
        true_label = test_db[i, -1]
        j = labels[predicted_label]
        k = labels[true_label]
        if true_label == predicted_label:
            correct_count += 1
            true_positive[j] += 1
        else:
            false_positive[j] += 1
            false_negative[k] += 1
        confusion_matrix[j, k] += 1
    accuracy = correct_count / N
    precision = np.zeros(n)
    recall = np.zeros(n)
    F1_measures = np.zeros(n)
    for i in range(n):
        precision[i] = true_positive[i] / (
            true_positive[i] + false_positive[i]
        )
        recall[i] = true_positive[i] / (
            true_positive[i] + false_negative[i]
        )
        F1_measures[i] = (2 * precision[i] * recall[i]) / (
            precision[i] + recall[i]
        )
    return (confusion_matrix, accuracy, precision, recall, F1_measures)


def evaluate(test_db, trained_tree):
    (N, k) = test_db.shape
    correct_count = 0
    for i in range(N):
        predicted_label = classify(test_db[i], trained_tree)
        true_label = test_db[i, -1]
        if true_label == predicted_label:
            correct_count += 1
    return correct_count / N
