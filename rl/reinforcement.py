from __future__ import annotations
from typing import TypeVar, Generic, Any, NamedTuple, List

from bidgame.framework.state import PrettyRepr

S = TypeVar('S')
A = TypeVar('A')
E = TypeVar('E')


class StateAction(Generic[S, A], NamedTuple, PrettyRepr):
    """
    - state: S - The current game state
    - action: A - Action that agent taken
    - next_state: S - The state of the game after next time step. None if it is terminate state.
    """
    state: S
    action: A
    next_state: S

    def updateSA(self, override_action: A = None, next_state: S = None) -> StateAction[S, A]:
        if override_action is not None:
            return StateAction(self.state, override_action, next_state)
        else:
            return StateAction(self.state, self.action, next_state)


class StateKeeper(Generic[S, A]):
    """
    Facilitate stateful to store series of StateAction[S, A]
    """

    def init_keeper(self):
        pass

    def update(self, a0: A, s1: S):
        pass

    def state_action(self) -> List[StateAction[S, A]]:
        pass


class RewardShaper(Generic[S, A, E]):
    def state_action_reward(self, end_result: E, sa_list: List[StateAction[S, A]]) -> List[float]:
        """
        - end_result: E - End game response
        - sa_list: List[StateAction[S, A]] - List of state transition usually work with StateKeeper.state_action
        """
        return [self._reward(sa.state, sa.next_state, sa.action, end_result) for sa in sa_list]

    def _reward(self, s0: S, s1: S, a: A, end_result: E) -> float:
        """
        Produce reward base on (s0,a) -> (s1, r)
        - s0: S - Start state
        - s1: S - Next state
        - a: A - Action taken in a step
        - end_result: E - End game response. Ususally use when s1 is None (aka terminated state).

        Return
        - reward score
            - positive reward encourage behaviour when you win, 0 when there is a draw
            - make sure that reward size for each game make sense e.g. how much you win/loss
        """
        pass
