class Player():
    def __init__(self, name, choice, won, drawn, lost, id = None):
        self.name = name
        self.choice = choice
        self.won = won
        self.drawn = drawn
        self.lost= lost
        self.id = id