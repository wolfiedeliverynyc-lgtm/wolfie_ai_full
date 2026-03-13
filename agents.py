class AIAgent:
    def __init__(self, name):
        self.name = name

    def act(self):
        return f'{self.name} is acting.'

class ChiefAI:
    def __init__(self, agent):
        self.agent = agent

    def oversee(self):
        return f'Chief AI is overseeing {self.agent.act()}.'