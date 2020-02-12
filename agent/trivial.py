from typing import List

from bidgame.framework.agent import BaseAgent
from bidgame.framework.state import Info

from rl.reinforcement import StateAction, Critic

# Observables state
# ====================
# Info(state=State(
# total_rounds:20,
# money:[1000, 991],
# profit_current:[0, 510],
# stars_current:[0, 51],
# stars_cumulative:[0, 462],
# current_round:18
# ), next_hotel=Hotel(stars=1, profit=40), previous_bids=Bids(bid0=10, bid1=972))


class ConstantAgent(BaseAgent):
    def step(self, info: Info) -> int:
        return 200


class PercentAgent(BaseAgent):
    def step(self, info: Info) -> int:
        ans = info.state.money[0]/4
        return int(ans)


class SimpleCritic(Critic[Info, int]):
    def _state_action_reward(self, end_result: float, sa_list: List[StateAction]) -> List[float]:
        return [self.__reward(sa.state, sa.action, end_result, sa.state.next_hotel is None) for sa in sa_list]

    def __reward(self, s: Info, a: int, end_result: float, is_terminate: bool) -> float:
        if is_terminate:
            return (end_result - 0.5) * 2
        return 0
