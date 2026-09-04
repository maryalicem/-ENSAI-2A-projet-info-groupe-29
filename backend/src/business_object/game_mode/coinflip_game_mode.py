import secrets
from game_mode.game_mode import GameMode
from business_object.player import Player
from business_object.game import Game
from datetime import datetime


class CoinFlipMode(GameMode):
    def play(self, p1: Player, p2: Player, choice: str = "heads") -> Game:
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=f"coinflip between {p1.username} and {p2.username}. Winner: {winner.username}",
            timestamp=datetime.now()
        )