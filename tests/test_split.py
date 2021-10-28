from split import find_split
from sample_datasets import one_instance_training_dataset, same_label_training_dataset

def test_one_instance_dataset_splits_from_last_value_for_every_attribute():
    split = find_split(one_instance_training_dataset)
    (N, k) = one_instance_training_dataset.shape
    assert split.split_value == N

def test_same_label_dataset_splits_from_last_value_for_every_attribute():
    split = find_split(same_label_training_dataset)
    (N, k) = same_label_training_dataset.shape
    assert split.split_value == N
