from competition_strategy import CompetitionStrategy

class Competitor:
    def __init__(self, strategy: CompetitionStrategy):
        self.strategy = strategy

    def compete(self):
        return self.strategy.compete()

    def display(self):
        return "displaying a competitor"