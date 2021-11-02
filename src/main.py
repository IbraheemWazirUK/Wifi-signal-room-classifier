from datasets import clean_dataset
from dtl import decision_tree_learning

(tree, depth) = decision_tree_learning(clean_dataset, 0)
print(depth)
