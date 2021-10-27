from dtl import decision_tree_learning
import numpy as np

one_instance_training_dataset = np.array([[1, 2, 3, 4, 5]])

same_label_training_dataset = np.array(
    [[1, 2, 5], [2, 3, 5], [4, 5, 5], [6, 7, 5], [8, 9, 5], [10, 11, 5]]
)


def test_one_instance_dataset_returns_leaf():
    (tree, depth) = decision_tree_learning(one_instance_training_dataset, 6)
    assert tree.is_leaf
    assert tree.value == 5
    assert depth == 6


def test_same_label_dataset_returns_leaf():
    (tree, depth) = decision_tree_learning(same_label_training_dataset, 15)
    assert tree.is_leaf
    assert tree.value == 5
    assert depth == 15
