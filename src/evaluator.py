from classifier import classify


def get_evaluation_metrics(test_db, trained_tree):
    (N, k) = test_db.shape
    correct_count = 0
    confusion_matrix = {}
    true_positive = {}
    false_negative = {}
    for i in range(N):
        predicted_label = classify(test_db[i], trained_tree)
        true_label = test_db[i, -1]
        if true_label == predicted_label:
            correct_count += 1
            true_positive[true_label] = true_positive.get(true_label, 0) + 1
        else:
            false_positive[predicted_label] = false_positive.get(predicted_label, 0) + 1
            false_negative[true_label] = false_negative.get(true_label, 0) + 1
        if predicted_label in confusion_matrix:
            if true_label in confusion_matrix[preidcted_label]:
                confusion_matrix[predicted_label][true_label] += 1
            else:
                confusion_matrix[predicted_label][true_label] = 1
        else:
            confusion_matrix[predicted_label] = {true_label: 1}
    accuracy = correct_count / N
    precision = {}
    recall = {}
    F1_measures = {}
    for label in confusion_matrix:
        precision[label] = true_positive[label] / (
            true_positive[label] + false_positive[label]
        )
        recall[label] = true_positive[label] / (
            true_positive[label] + false_negative[label]
        )
        F1_measures[label] = (2 * precision[label] * recall[label]) / (
            precision[label] + recall[label]
        )
    return (confusion_matrix, accuracy, precision, recall, F1_measures)


def evaluate(test_db, trained_tree):
    (cm, acc, p, r, f) = get_evaluation_metrics(test_db, trained_tree)
    return acc
