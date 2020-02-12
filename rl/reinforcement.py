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


class RewardShaper(Environment[S, A]):
    def state_action_reward(self, sa: List[StateAction[S, A]]) -> List[float]:
        pass
