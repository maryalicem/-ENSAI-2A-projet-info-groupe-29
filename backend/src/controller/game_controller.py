from fastapi import APIRouter, Depends

from schema.game_model import GamePlayModel, GameResponse
from service.game_service import GameService
from utils.log_utils import get_logger
from utils.security import verify_token

router = APIRouter()

logger = get_logger(__name__)


def get_game_service():
    """Dependency provider for GameService."""
    return GameService()


@router.post("/", response_model=GameResponse, tags=["Games"])
def play_game(
    req: GamePlayModel, game_service=Depends(get_game_service), current_player=Depends(verify_token)
):
    """Starts and executes a new game session.
    Args:
        req (GamePlayModel): Request containing player IDs and game mode.
        game_service (GameService): Service handling game logic.
        current_player (Player): The authenticated user.
    Returns:
        GameResponse: Match summary including player usernames, result, winner,
            and updated ELO ratings.
    Raises:
        HTTPException: 401 if unauthenticated, 400 if invalid request.
    """
    logger.info("Play a game")
    
    # Appel de la méthode play() avec req.game_mode en 3ème position
    # (On conserve **req.params à la fin si le modèle attend d'autres paramètres futurs)
    game = game_service.play(
        current_player.id_player, 
        req.id_opponent, 
        req.game_mode, 
        **req.params if hasattr(req, 'params') and req.params else {}
    )

    # Utilisation de l'objet Game retourné pour hydrater le GameResponse
    return GameResponse(
        username1=game.player1.username,
        username2=game.player2.username,
        description=game.description,
        winner=game.winner.username if game.winner else None,
        new_elo1=game.player1.elo,
        new_elo2=game.player2.elo,
    )