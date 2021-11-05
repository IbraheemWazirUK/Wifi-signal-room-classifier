from tree import Tree
from evaluator import evaluate


def get_validation_error(validation_db, trained_tree):
    acc = evaluate(validation_db, trained_tree)
    return 1 - acc


def prune(cur_tree, validation_db, trained_tree):
    l_branch = cur_tree.l_branch
    r_branch = cur_tree.r_branch
    og_value = cur_tree.value
    if l_branch != None and l_branch.is_leaf and r_branch != None and r_branch.is_leaf:
        pre_pruning_ve = get_validation_error(validation_db, trained_tree)
        cur_tree.l_branch = None
        cur_tree.r_branch = None
        cur_tree.value = l_branch.value
        cur_tree.is_leaf = True
        left_pruning_ve = get_validation_error(validation_db, trained_tree)
        cur_tree.value = r_branch.value
        right_pruning_ve = get_validation_error(validation_db, trained_tree)
        min_ve = min(pre_pruning_ve, left_pruning_ve, right_pruning_ve)
        tree_changed = True
        if min_ve == left_pruning_ve:
            cur_tree.value = l_branch.value
        elif min_ve == pre_pruning_ve:
            cur_tree.l_branch = l_branch
            cur_tree.r_branch = r_branch
            cur_tree.value = og_value
            cur_tree.is_leaf = False
            tree_changed = False
        if tree_changed:
            if cur_tree.parent != None:
                prune(cur_tree.parent, validation_db, trained_tree)
    else:
        if l_branch != None:
            prune(l_branch, validation_db, trained_tree)
        if r_branch != None:
            prune(r_branch, validation_db, trained_tree)
