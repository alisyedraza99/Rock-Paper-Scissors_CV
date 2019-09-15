
class Player:
    def __init__(self, name):
        self.play = None
        self.name = name
    
    def set_play(self, value):
        self.play = value 
    
    def get_play(self):
        return self.play

    def get_name(self):
        return self.name

if __name__ == "__main__":
    p = Player()
    p.set_play("rock")
    print(p.get_play())
