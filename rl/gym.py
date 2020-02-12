from typing import NewType, NamedTuple, Tuple, List

from bidgame.framework.agent import BaseAgent
from bidgame.framework.game import Game, ValueDist
from bidgame.framework.state import State, Hotel, Bids, Info
from bidgame.framework.gui import GameGui

from .reinforcement import StateAction, Environment

# import logging
# from copy import deepcopy
import numpy as np
# import time


def play_single_game_debug(
    players1: BaseAgent,
    players2: BaseAgent,
    render: bool = False,
    dists: ValueDist = ValueDist(),
) -> Tuple[float, List[StateAction]]:
    """
      Play one game given two agents.
      :param players: 2 agents to play against each other
      :param render: if should use the visual GUI
      :param dists: random distributions for the random elements in the game
      :return: result of the game, series of state-action pair trajector
      """

    players = (players1, players2)

    game = DebugGame(game_gui=None, dists=dists)

    infos = game.start()
    while True:
        bids = [p.step(i) for p, i in zip(players, infos)]
        infos = game.step(*bids)

        end_result = infos[0].state.get_end_result()
        if end_result is not None:
            return end_result, game.state_action()


class DebugGame(Game, Environment[State, int]):
    def __init__(
        self,
        dists: ValueDist = ValueDist(),
        hotel_stars: np.ndarray = None,
        hotel_profit: np.ndarray = None,
        initial_state: State = None,
        game_gui: GameGui = None,
    ):
        super().__init__(dists, hotel_stars, hotel_profit, initial_state, game_gui)
        self.sa = []

    def start(self) -> Tuple[Info, Info]:
        self._log(f"Start game: {self.state}")
        info = self._build_info()
        self.update(None, info[0])
        return info

    def step(self, bid0: int, bid1: int) -> Tuple[Info, Info]:
        next_hotel = self._get_next_hotel()
        self._log(f"Next up {next_hotel} {self.state}")
        if self.game_gui is not None:
            human_bids = self.game_gui.update_gui(
                state=self.state, next_hotel=next_hotel, realized_bids=None
            )
            bid0 = human_bids[0] if human_bids[0] is not None else bid0
            bid1 = human_bids[1] if human_bids[1] is not None else bid1

        realized_bids = Bids(
            *(
                min(_to_int_or_zero(b), m)
                for b, m in zip([bid0, bid1], self.state.money)
            )
        )

        self._log(f"Got {realized_bids}")

        winner_idx = realized_bids.winner_idx
        winning_bid = realized_bids.winning_bid

        if winner_idx is not None:
            self._log(
                f"Player {winner_idx} wins the auction and pays {winning_bid}")
            self.state.money[winner_idx] -= winning_bid
            self.state.stars_current[winner_idx] += next_hotel.stars
            self.state.profit_current[winner_idx] += next_hotel.profit
        else:
            self._log("No auction winner, hotel is skipped")

        if self.game_gui is not None:
            self.game_gui.update_gui(
                state=self.state, next_hotel=next_hotel, realized_bids=realized_bids
            )

        self.state.update()
        if self.state.rounds_left == 0:
            self._log(f"Game is finished, last state {self.state}")
            self._log(f"Result: {self.state.get_end_result()}")
            if self.game_gui is not None:
                self.game_gui.update_gui(
                    state=self.state, next_hotel=None, realized_bids=None
                )

        info = self._build_info(realized_bids)
        self.update(bid0, info[0])
        return info

    def update(self, a0: int, s1: State):
        if len(self.sa) > 0 and a0 is not None:
            self.sa[-1] = self.sa[-1].copy(a0)
        self.sa.append(StateAction(state=s1, action=None))

    def state_action(self) -> List[StateAction]:
        return self.sa


def _random_choice_from(values, size=None):
    if isinstance(values, int):
        return values
    elif isinstance(values, (list, tuple, float, np.ndarray)):
        return np.random.choice(values, size=size)
    else:
        raise ValueError(
            f"values should be int or array-like, got {type(values)} - {values}"
        )


def _to_int_or_zero(x):
    try:
        return int(x)
    except ValueError:
        return 0
