from tree import Tree
from split import find_split


def decision_tree_learning(training_dataset, depth):
    if len(training_dataset) == 0:
        raise ValueError("training_dataset can't be empty")
    labels = [training_instance[-1] for training_instance in training_dataset]
    if labels and labels.count(labels[0]) == len(labels):
        return (Tree(labels[0], None, None, None, True), depth)
    (split_rule, l_dataset, r_dataset) = find_split(training_dataset)
    (l_branch, l_depth) = decision_tree_learning(l_dataset, depth + 1)
    (r_branch, r_depth) = decision_tree_learning(r_dataset, depth + 1)
    tree = Tree(split_rule, None, l_branch, r_branch)
    return (tree, max(l_depth, r_depth))
