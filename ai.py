
from abc import ABC, abstractmethod

# Abstract base class for AI players
class AIPlayer(ABC):
    @abstractmethod
    def choose_move(self, board, mark):
        pass

# Easy AI chooses a random empty cell
class EasyAI(AIPlayer):
    def __init__(self, rng):
        self.rng = rng

    def choose_move(self, board, mark):
        return self.rng.choice(board.empty_cells())
