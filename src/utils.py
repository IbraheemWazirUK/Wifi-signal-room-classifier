def add_parents(cur_tree, parent):
    cur_tree.parent = parent
    if cur_tree.l_branch != None:
        add_parents(cur_tree.l_branch, cur_tree)
    if cur_tree.r_branch != None:
        add_parents(cur_tree.r_branch, cur_tree)

def get_tree_depth(cur_tree, depth):
    r_depth = 0
    l_depth = 0
    if cur_tree.l_branch:
        l_depth = get_tree_depth(cur_tree.l_branch, depth+1)
    if cur_tree.r_branch:
        r_depth = get_tree_depth(cur_tree.r_branch, depth+1)
    return max(depth, l_depth, r_depth)
