from agent.constant_agent import ConstantAgent
from bidgame.example_agents import SmartAgent
from bidgame.framework.playing import play_series

result_against_smart = play_series(
    (SmartAgent(), ConstantAgent()),
    max_games=10000,
    # we won't play all 1000 games
    # if one agent reaches probability > 0.9999
    # to be better than the other agent
    prob_stopping_threshold=1 - 0.9999
)

print(result_against_smart.iloc[-1])
