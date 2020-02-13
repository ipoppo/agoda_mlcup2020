from typing import List

from bidgame.framework.state import Info

from rl.reinforcement import StateAction, RewardShaper


class SimpleScore(RewardShaper[Info, int, float]):
    def _reward(self, s0: Info, s1: Info, a: int, end_result: float) -> float:
        if s1 is None:
            return (0.5 - end_result) * 2

        else:
            return 0


class WeightedStarScore(RewardShaper[Info, int, float]):

    def __init__(self, end_result_weight: float = 0, star_weight: float = 1):
        assert(end_result_weight > 0,
               "end_result_weight must be non-negative")
        assert(star_weight > 0,
               "star_weight must be non-negative")
        assert(end_result_weight+star_weight > 0,
               "Total weight must be greater than zero")

        self.end_result_weight = end_result_weight
        self.star_weight = star_weight

    def _reward(self, s0: Info, s1: Info, a: int, end_result: float) -> float:
        if s1 is None:
            if end_result == 0.5:
                return 0

            end_result_score = (0.5 - end_result) * 2

            print(s0)
            star = s0.state.stars_cumulative
            star_score = (star[0] - star[1]) / (star[0] + star[1])
            return (end_result_score*self.end_result_weight + star_score*self.star_weight) / (self.end_result_weight + self.star_weight)

        else:
            return 0
