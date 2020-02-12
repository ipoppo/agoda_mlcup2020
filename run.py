from agent.trivial import ConstantAgent, PercentAgent
from agent.critic import SimpleCritic
from bidgame.example_agents import SmartAgent
from bidgame.framework.agent import HumanAgent
from bidgame.framework.playing import play_series
from rl.gym import play_single_game_debug


def main():
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

    end_result, sa = play_single_game_debug(ConstantAgent(), SmartAgent())

    print('RESULT')
    print(end_result)
    print('SA')
    print(sa)

    critic = SimpleCritic()
    rewards = critic.state_action_reward(end_result, sa)

    print('REWARDS')
    print(rewards)


if __name__ == "__main__":
    main()
