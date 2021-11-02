from split import find_split
from sample_datasets import (
    one_instance_training_dataset,
    same_label_training_dataset,
    example_training_dataset,
    example_training_dataset2,
)


def test_one_instance_dataset_splits_from_last_value_for_every_attribute():
    (split, l_dataset, r_dataset) = find_split(one_instance_training_dataset)
    (N, k) = one_instance_training_dataset.shape
    assert l_dataset.shape == (N, k)
    assert r_dataset.shape == (0, k)


def test_same_label_dataset_splits_from_last_value_for_every_attribute():
    (split, l_dataset, r_dataset) = find_split(same_label_training_dataset)
    (N, k) = same_label_training_dataset.shape
    assert l_dataset.shape == (N, k)
    assert r_dataset.shape == (0, k)


def test_example_dataset_returns_correct_split():
    (split, l_dataset, r_dataset) = find_split(example_training_dataset)
    assert split.attribute == 0
    assert split.split_value == 4


def test_example_dataset_returns_correct_split_twice():
    (split, l_dataset, r_dataset) = find_split(example_training_dataset)
    (split2, l_dataset2, r_dataset2) = find_split(l_dataset)
    assert split2.attribute == 0
    assert split2.split_value == 1


def test_example_two_returns_correct_split():
    (split, l_dataset, r_dataset) = find_split(example_training_dataset2)
    print(split)
    assert l_dataset.shape == r_dataset.shape
