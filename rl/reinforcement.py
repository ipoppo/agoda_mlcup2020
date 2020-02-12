from __future__ import annotations
from typing import TypeVar, Generic, Any, NamedTuple, List

from bidgame.framework.state import PrettyRepr

S = TypeVar('S')
A = TypeVar('A')


class StateAction(Generic[S, A], NamedTuple, PrettyRepr):
    state: S
    action: A
    next_state: S

    def updateSA(self, override_action: A = None, next_state: S = None) -> StateAction[S, A]:
        if override_action is not None:
            return StateAction(self.state, override_action, next_state)
        else:
            return StateAction(self.state, self.action, next_state)


class Environment(Generic[S, A]):
    def update(self, a0: A, s1: S):
        pass

    def state_action(self) -> List[StateAction[S, A]]:
        pass


class Critic(Generic[S, A]):
    def state_action_reward(self, end_result: float, sa_list: List[StateAction[S, A]]) -> List[float]:
        return [self._reward(sa.state, sa.next_state, sa.action, end_result) for sa in sa_list]

    def _reward(self, s0: S, s1: S, a: A, end_result: float) -> float:
        pass
