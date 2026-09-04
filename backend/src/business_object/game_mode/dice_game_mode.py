import random
from game_mode.game_mode import GameMode
from business_object.player import Player
from business_object.game import Game
from datetime import datetime


class DiceMode(GameMode):

    def play(p1: Player, p2: Player):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 > dice2:
            winner = p1
        elif dice2 > dice1:
            winner = p2
        else:
            winner = None
        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description=f"Dice roll between {p1.username} and {p2.username}. Winner: {winner.username}",
            timestamp=datetime.now()
        )