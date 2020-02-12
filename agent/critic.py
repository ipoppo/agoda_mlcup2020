from typing import List

from bidgame.framework.state import Info

from rl.reinforcement import StateAction, Critic


class SimpleCritic(Critic[Info, int, float]):
    def _reward(self, s0: Info, s1: Info, a: int, end_result: float) -> float:
        if s1 is None:
            return (end_result - 0.5) * 2
        else:
            return 0
