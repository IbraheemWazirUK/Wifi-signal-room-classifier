from tree import Tree


def decision_tree_learning(training_dataset, depth):
    if len(training_dataset) == 0:
        raise ValueError("training_dataset can't be empty")
    labels = [training_instance[-1] for training_instance in training_dataset]
    if labels and labels.count(labels[0]) == len(labels):
        return (Tree(labels[0], None, None, True), depth)
    return (Tree(None, None, None), 0)
