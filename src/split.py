from splitrule import SplitRule
import numpy as np
import math


def get_labels(ys):
    labels = {}
    for y in ys:
        if y in labels:
            labels[y] += 1
        else:
            labels[y] = 1
    return labels


def split(x_sorted, j):
    return (x_sorted[: j + 1], x_sorted[j + 1 :])


def H(label_count, total):
    res = 0
    for label in label_count:
        p = label_count[label] / total
        if p != 0:
            res -= p * math.log(p, 2)
    return res


def calculate_information_gain(
    H_dataset,
    l_branch,
    r_branch,
    labels_left_count,
    labels_right_count,
    labels_left_total,
    labels_right_total,
):
    H_left = H(labels_left_count, labels_left_total)
    H_right = H(labels_right_count, labels_right_total)
    total = labels_left_total + labels_right_total
    remainder = H_left * (labels_left_total / total) + H_right * (
        labels_right_total / total
    )
    return H_dataset - remainder


def find_split(training_dataset):
    y_training = training_dataset[:, -1]
    labels_training_count = get_labels(y_training)
    x_training = training_dataset[:, :-1]
    (N, k) = x_training.shape
    best_split_rule = None
    cur_split_rule = None
    best_ldataset = None
    best_rdataset = None
    max_information_gain = -1
    H_dataset = H(labels_training_count, N)
    for i in range(k):
        arg_sort = np.argsort(x_training[:, i])
        y_sorted = y_training[arg_sort]
        x_sorted = x_training[arg_sort]
        training_sorted = training_dataset[arg_sort]
        labels_left_count = {}
        labels_right_count = labels_training_count.copy()
        labels_left_total = 0
        for j in range(N):
            sorted_column = x_sorted[:, i]
            if j < N - 1:
                if sorted_column[j] == sorted_column[j + 1]:
                    if y_sorted[j] in labels_left_count:
                        labels_left_count[y_sorted[j]] += 1
                    else:
                        labels_left_count[y_sorted[j]] = 1
                    labels_left_total += 1
                    labels_right_count[y_sorted[j]] -= 1
                    continue
                if y_sorted[j] in labels_left_count:
                    labels_left_count[y_sorted[j]] += 1
                else:
                    labels_left_count[y_sorted[j]] = 1
                labels_left_total += 1
                labels_right_count[y_sorted[j]] -= 1
            cur_split_rule = SplitRule(i, sorted_column[j])
            (l_dataset, r_dataset) = split(training_sorted, j)
            labels_right_total = N - labels_left_total
            info_gain = calculate_information_gain(
                H_dataset,
                l_dataset,
                r_dataset,
                labels_left_count,
                labels_right_count,
                labels_left_total,
                labels_right_total,
            )
            if info_gain >= max_information_gain:
                max_information_gain = info_gain
                best_split_rule = cur_split_rule
                best_ldataset = l_dataset
                best_rdataset = r_dataset
    return (best_split_rule, best_ldataset, best_rdataset)
