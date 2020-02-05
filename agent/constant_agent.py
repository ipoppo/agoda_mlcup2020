from bidgame.framework.agent import BaseAgent
from bidgame.framework.state import Info


class ConstantAgent(BaseAgent):
    def step(self, info: Info) -> int:

        # Observables state
        # ====================
        # Info(state=State(
        # total_rounds:20,
        # money:[1000, 991],
        # profit_current:[0, 510],
        # stars_current:[0, 51],
        # stars_cumulative:[0, 462],
        # current_round:18
        # ), next_hotel=Hotel(stars=1, profit=40), previous_bids=Bids(bid0=10, bid1=972))

        return 20
