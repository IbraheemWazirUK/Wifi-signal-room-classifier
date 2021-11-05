class Tree:
    def __init__(self, value, parent=None, l_branch=None, r_branch=None, is_leaf=False):
        self.value = value
        self.l_branch = l_branch
        self.r_branch = r_branch
        self.is_leaf = is_leaf
        self.parent = parent

