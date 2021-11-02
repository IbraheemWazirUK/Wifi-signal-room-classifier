import numpy as np


def divide_into_folds(dataset, k, rng):
    db = np.copy(dataset)
    rng.shuffle(db)
    return np.split(db, k)

def create_k_models(dataset, k, rng):
    folds = divide_into_folds(dataset, k, rng)
    models = []
    for i in range(len(folds)):
        test_dataset = folds[i]
        training_dataset = np.concatenate(
            [fold for j, fold in enumerate(folds) if j != i]
        )
        models.append((test_dataset, training_dataset))
    return models
