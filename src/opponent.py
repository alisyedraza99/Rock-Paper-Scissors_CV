import random
class Opponent:
    def __init__(self):
        self.play = None
        self.options = ["paper", "rock", "scissor"]
    
    def set_play(self):
        self.play = self.options[random.randrange(len(self.options))]
    
    def set_none(self):
        self.play = "..."

    def get_play(self):
        return self.play

if __name__ == "__main__":
    op = Opponent()
    op.set_play()
    print(op.get_play())