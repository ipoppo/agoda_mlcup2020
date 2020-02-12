from typing import List

from bidgame.framework.state import Info

from rl.reinforcement import StateAction, Critic


class SimpleCritic(Critic[Info, int]):
    def _state_action_reward(self, end_result: float, sa_list: List[StateAction]) -> List[float]:
        return [self.__reward(sa.state, sa.action, end_result, sa.state.next_hotel is None) for sa in sa_list]

    def __reward(self, s: Info, a: int, end_result: float, is_terminate: bool) -> float:
        if is_terminate:
            return (end_result - 0.5) * 2
        return 0
