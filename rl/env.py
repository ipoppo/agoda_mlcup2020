from gym import error, spaces
from gym.utils import seeding
import numpy as np

import gym


class BidGameEnv(gym.Env):
    def __init__(self, fraction=True):
        if fraction:
            self.action_space = spaces.Box(
                np.array([0]), np.array([1]), dtype=np.float32)
        else:
            self.action_space = spaces.Box(
                np.array([0]), np.array([np.inf]), dtype=np.int)

        # p0 = opponenet, p1 = me
        tr_l, tr_u = 0, np.inf              # info.state.total_rounds
        m0_l, m0_u = 0, np.inf              # info.state.money[0]
        m1_l, m1_u = 0, np.inf              # info.state.money[1]
        p0_l, p0_u = 0, np.inf              # info.state.profit_current[0]
        p1_l, p1_u = 0, np.inf              # info.state.profit_current[1]
        s0_l, s0_u = 0, np.inf              # info.state.stars_current[0]
        s1_l, s1_u = 0, np.inf              # info.state.stars_current[1]
        c0_l, c0_u = 0, np.inf              # info.state.stars_cumulative[1]
        c1_l, c1_u = 0, np.inf              # info.state.stars_cumulative[1]
        cr_l, cr_u = 0, np.inf              # info.state.current_round
        hs_l, hs_u = -np.inf, np.inf        # info.next_hotel.stars
        hp_l, hp_u = -np.inf, np.inf        # info.next_hotel.profit
        b0_l, b0_u = 0, np.inf              # info.previous_bids.bid0
        b1_l, b1_u = 0, np.inf              # info.previous_bids.bid1

        self.observation_space = spaces.Box(
            np.array([tr_l, m0_l, m1_l, p0_l, p1_l, s0_l, s1_l,
                      c0_l, c1_l, cr_l, hs_l, hp_l, b0_l, b1_l]),
            np.array([tr_u, m0_u, m1_u, p0_u, p1_u, s0_u, s1_u,
                      c0_u, c1_u, cr_u, hs_u, hp_u, b0_u, b1_u]),
            dtype=np.int
        )

    def step(self, action):
        pass

    def reset(self):
        pass

    def _set_action_space(self):
        pass
        # bounds = self.model.actuator_ctrlrange.copy()
        # low, high = bounds.T
        # self.action_space = spaces.Box(low=low, high=high, dtype=np.float32)
        # return self.action_space

    def _set_observation_space(self, observation):
        pass
        # self.observation_space = convert_observation_to_space(observation)
        # return self.observation_space

    def seed(self, seed=None):
        pass
        # self.np_random, seed = seeding.np_random(seed)
        # return [seed]

    # ob = env.reset()
    # ob_next, reward, done, info = env.step(action)
