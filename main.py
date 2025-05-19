from game import Game
from agent import QLearningAgent
import pygame

# Configs
WIDTH, HEIGHT = 15, 10
EPISODES = 100000
SHOW_GAME = False  # Set to False if you don't want game rendering

# Initialize game and agent
game = Game(WIDTH, HEIGHT)
agent = QLearningAgent(WIDTH, HEIGHT,alpha=0.5, gamma=0.98, epsilon=0.2)
agent.load_q_table()

# Stats
success_streak = 0
consecutive_success_required = 10

for episode in range(1, EPISODES + 1):
    state = game.reset()
    done = False
    total_reward = 0

    while not done:
        if SHOW_GAME:
            game.render()

        action = agent.select_action(state)
        next_state, reward, done = game.step(action)
        agent.learn(state, action, reward, next_state)

        state = next_state
        total_reward += reward

    if (episode + 1) % 1000 == 0:
        agent.save_q_table("q_table.pkl")

    if reward == 1:
        success_streak += 1
    else:
        success_streak = 0

    print(f"Episode {episode} | Reward: {total_reward} | Success Streak: {success_streak}")

    if success_streak == consecutive_success_required:
        print("Harry escaped successfully 10 times in a row!")
        break

agent.save_q_table()

pygame.quit()
