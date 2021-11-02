class SplitRule:
    def __init__(self, attribute, split_value):
        self.attribute = attribute
        self.split_value = split_value

    def __str__(self):
        return "A" + str(self.attribute) + " > " + str(self.split_value)
