import random
import pickle
from collections import defaultdict

class QLearningAgent:
    def __init__(self, width, height, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table1 = defaultdict(lambda: [0, 0, 0, 0])
        self.width = width
        self.height = height

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        return self._argmax(self.q_table1[state])

    def learn(self, state, action, reward, next_state):
        max_future_q = max(self.q_table1[next_state])
        self.q_table1[state][action] += self.alpha * (
            reward + self.gamma * max_future_q - self.q_table1[state][action]
        )

    def _argmax(self, lst):
        max_val = max(lst)
        return random.choice([i for i, val in enumerate(lst) if val == max_val])

    def save_q_table(self, filename="q_table1.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(dict(self.q_table1), f)

    def load_q_table(self, filename="q_table1.pkl"):
        try:
            with open(filename, "rb") as f:
                loaded_table = pickle.load(f)
                self.q_table1 = defaultdict(lambda: [0, 0, 0, 0], loaded_table)
        except FileNotFoundError:
            print("No saved Q-table found. Starting fresh.")

