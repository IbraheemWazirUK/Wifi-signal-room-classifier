class Tree:
    def __init__(self, value, l_branch, r_branch, is_leaf=False):
        self.value = value
        self.l_branch = l_branch
        self.r_branch = r_branch
        self.is_leaf = is_leaf
