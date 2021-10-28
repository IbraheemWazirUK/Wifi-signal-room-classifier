import numpy as np

one_instance_training_dataset = np.array([[1, 2, 3, 4, 5]])

same_label_training_dataset = np.array(
    [[1, 2, 5], [2, 3, 5], [4, 5, 5], [6, 7, 5], [8, 9, 5], [10, 11, 5]]
)

example_training_dataset = np.array(
    [
        [1, 3, 0],
        [1, 4, 0],
        [1, 6, 0],
        [1, 7, 0],
        [2, 3, 1],
        [2, 5, 0],
        [2, 6, 0],
        [3, 3, 1],
        [3, 4, 0],
        [3, 6, 1],
        [3, 7, 0],
        [4, 4, 1],
        [4, 5, 1],
        [4, 7, 0],
        [5, 3, 1],
        [5, 6, 1],
        [5, 7, 1],
        [6, 4, 1],
        [6, 5, 1],
        [6, 7, 1],
    ]
)

example_tree_dataset = np.array(
    [[0, 0, 0], [0, 2, 0], [0, 3, 0], [1, 0, 1], [1, 1, 1], [1, 2, 2], [1, 3, 2]]
)
