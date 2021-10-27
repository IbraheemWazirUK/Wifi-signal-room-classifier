from datasets import noisy_dataset, clean_dataset
import numpy as np


def test_datasets_loaded_correctly():
    assert noisy_dataset.shape == (2000, 8)
    assert clean_dataset.shape == (2000, 8)
