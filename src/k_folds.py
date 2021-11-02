import numpy as np


def divide_into_folds(dataset, k=10, rng=np.default_rng()):
    return rng.choice(dataset, size=k, replace=False)


def create_k_models(dataset, k=10, rng=np.default_rng()):
    folds = divide_into_folds(dataset, k, rng)
    model = []
    for i in range(folds):
        test_dataset = folds[i]
        training_dataset = np.concatenate(
            [fold for j, fold in enumerate(folds) if j != i]
        )
        model.append((test_dataset, training_dataset))
