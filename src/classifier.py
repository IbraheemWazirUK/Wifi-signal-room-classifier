def classify(test_instance, trained_tree):
    cur_tree = trained_tree
    while not cur_tree.is_leaf:
        if test_intsance[split_rule.attribute] > split_rule.split_value:
            cur_tree = cur_tree.r_branch
        else:
            cur_tree = cur_tree.l_branch
    return cur_tree.value
