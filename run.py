import numpy as np
import torch
import gym

from agent.trivial import ConstantAgent, PercentAgent
from agent.critic import SimpleScore, WeightedStarScore
from bidgame.example_agents import SmartAgent
from bidgame.framework.agent import HumanAgent
from bidgame.framework.playing import play_series
from rl.arguments import get_args
from rl.debug import play_single_game_debug
from rl.model import A2CNet


def main():
    ## ============================================= ##
    # SETUP Pytorch
    ## ============================================= ##
    args = get_args()
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)

    if args.cuda and torch.cuda.is_available() and args.cuda_deterministic:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True

    torch.set_num_threads(1)
    device = torch.device("cuda:0" if args.cuda else "cpu")

    ## ============================================= ##
    # MAIN
    ## ============================================= ##

    # result_against_smart = play_series(
    #     (SmartAgent(), ConstantAgent()),
    #     max_games=10000,
    #     # we won't play all 1000 games
    #     # if one agent reaches probability > 0.9999
    #     # to be better than the other agent
    #     prob_stopping_threshold=1 - 0.9999
    # )

    # print(result_against_smart)
    # print(result_against_smart.iloc[-1])

    # end_result, sa = play_single_game_debug(PercentAgent(), SmartAgent())

    # # critic = WeightedStarScore(star_weight=0.1)
    # critic = SimpleScore()
    # rewards = critic.state_action_reward(end_result, sa)

    # print('REWARDS')
    # print(rewards)

    model = A2CNet(10)

    print(model)

    x = np.array([np.zeros(10), np.ones(10)])
    y = model(x)

    print(y)


if __name__ == "__main__":
    main()
