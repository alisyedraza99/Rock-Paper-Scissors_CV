from opponent import Opponent
from player import Player

class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.winner = ""
    
    def decide_winner(self):
        op_hand = self.opponent.get_play()
        p_hand = self.player.get_play()

        if (op_hand == "rock" and p_hand == "paper"):
            self.winner = self.player.get_name()
        elif (op_hand == "paper" and p_hand == "rock"):
             self.winner = "Opponent"
        elif (op_hand == "paper" and p_hand == "scissor"):
             self.winner = self.player.get_name()
        elif (p_hand == "paper" and op_hand == "scissor"):
             self.winner = "Opponent"
        elif (op_hand == "scissor" and p_hand == "rock"):
             self.winner = self.player.get_name()
        elif (p_hand == "scissor" and op_hand == "rock"):
             self.winner = "Opponent"
        else:
            self.winner = "draw"
        
        return self.winner
    
    def get_winner(self):
        return self.winner

if __name__ == "__main__":
    p = Player("ali")
    op = Opponent()
    game = Game(p, op)
    op.set_play()
    print("AI played", op.get_play())
    p.set_play("rock")
    print("You played", p.get_play())
    winner = game.decide_winner()
    print(winner)

    