from fastapi import HTTPException

from dao.player_dao import PlayerDao
from game_mode.game_mode_factory import GameModeFactory
from scoring.scoring_strategy import ScoringStrategy
from utils.log_utils import log

class GameService:
    """Service that manages games."""

    @log
    def play(self, id_player: int, id_opponent: int, game_mode: str, **kwargs):
        """Executes a single round of a game between two players.
        """
        # 1. Get players (nothing to change)
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        if not p1 or not p2:
            raise HTTPException(status_code=404, detail="Player not found")

        # 2. Get the game mode using the factory
        mode = GameModeFactory.get_mode(game_mode)

        # 3. Play the game
        game = mode.play(p1, p2)

        # 4. Update elo of both players
        ScoringStrategy.update_player_ratings(game)

        PlayerDao().update(p1)
        PlayerDao().update(p2)

        # 5. Return a Game object
        return game