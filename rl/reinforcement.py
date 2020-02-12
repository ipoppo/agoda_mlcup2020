from __future__ import annotations
from typing import TypeVar, Generic, Any, NamedTuple, List

S = TypeVar('S')
A = TypeVar('A')


class StateAction(Generic[S, A], NamedTuple):
    state: S
    action: A

    def copy(self, override_action: A) -> StateAction[S, A]:
        if override_action is not None:
            return StateAction(self.state, override_action)
        else:
            return StateAction(self.state, self.action)


class Environment(Generic[S, A]):
    def update(self, a0: A, s1: S):
        pass

    def state_action(self) -> List[StateAction[S, A]]:
        pass


class Critic(Generic[S, A]):
    def state_action_reward(self, end_result: float, sa_list: List[StateAction[S, A]]) -> List[float]:
        reward_list = self._state_action_reward(end_result, sa_list)
        error_txt = "Reward function should have returned same length as State Action list"
        assert len(reward_list) == len(sa_list), error_txt
        return reward_list

    def _state_action_reward(self, end_result: float, sa_list: List[StateAction[S, A]]) -> List[float]:
        pass
