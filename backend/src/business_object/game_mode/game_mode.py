from abc import ABC, abstractmethod
from business_object.player import Player
from business_object.game import Game

class GameMode(ABC):

    @abstractmethod
    def play(self, p1: Player, p2: Player) -> Game:
        pass