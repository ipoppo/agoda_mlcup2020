from bidgame.framework.agent import BaseAgent
from bidgame.framework.state import Info


class ConstantAgent(BaseAgent):
    def step(self, info: Info) -> int:
        return 10
