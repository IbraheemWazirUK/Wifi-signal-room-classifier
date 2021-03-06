from dtl import decision_tree_learning
from sample_datasets import (
    one_instance_training_dataset,
    same_label_training_dataset,
    example_tree_dataset,
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


def test_decision_tree_generated_correctly():
    (tree, depth) = decision_tree_learning(example_tree_dataset, 0)
    assert depth == 2
    assert tree.l_branch.is_leaf
