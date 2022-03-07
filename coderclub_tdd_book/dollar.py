class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount*multiplier)

    def equals(self, dollar):
        # TODO: make sure dollar is a dollar?
        return self.amount == dollar.amount
