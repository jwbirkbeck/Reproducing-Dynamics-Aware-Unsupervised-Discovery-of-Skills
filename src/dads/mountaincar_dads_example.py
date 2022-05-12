import torch
from agent.DADSAgent import DADSAgent
from src.soft_actor_critic.environments.mountaincar_cont import MountainCarContinuous

env = MountainCarContinuous()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

agent = DADSAgent(env=env, device=device, n_skills=4, learning_rate=0.01)

t = 0
while t < 500:
    t += 1
    agent.play_games(1, verbose=True)

agent.play_games(1, verbose=False, display_gameplay=True, skill=0)
agent.play_games(1, verbose=False, display_gameplay=True, skill=1)
agent.play_games(1, verbose=False, display_gameplay=True, skill=2)
agent.play_games(1, verbose=False, display_gameplay=True, skill=3)

print("done!")