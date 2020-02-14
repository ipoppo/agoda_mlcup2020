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

    def __init__(self, star_weight: float = 0.1):
        assert star_weight >= 0 and star_weight <= 1, "star_weight must be >= 0 AND <= 1"
        self.star_weight = star_weight
        self.reset()

    def reset(self):
        self.cum_max_star = 0

    def _reward(self, s0: Info, s1: Info, a: int, end_result: float) -> float:
        if s1 is None:
            if end_result == 0.5:
                return 0

            # -1 = Loss, 1 = Win
            end_result_score = (1 - end_result) * 2 - 1

            # -1 = get no stars, 1 = get all stars
            star_score = \
                (s0.state.stars_cumulative[0] / self.cum_max_star) * 2 - 1

            print(s0.state.stars_cumulative)
            return (1 - self.star_weight) * end_result_score + self.star_weight * star_score

        else:
            self.cum_max_star += s0.next_hotel.stars * \
                (s0.state.total_rounds - s0.state.current_round)
            return 0
