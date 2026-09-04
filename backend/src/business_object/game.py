class Game:
    def __init__(
        self,
        id_game,
        player1,
        player2,
        game_mode,
        winner,
        description,
        timestamp
    ):
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.time_stamp = timestamp

    def __str__(self):
        return f"{self.game_mode} between {self.player1.username} and {self.player2.username}. Winner is {self.winner.username} !"


