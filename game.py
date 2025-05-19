import pygame
import random
from bfs import bfs

CELL_SIZE = 50
WALL = 'X'

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))
        pygame.display.set_caption("Goblet of Fire RL")

        self.clock = pygame.time.Clock()
        self.walls = set()
        self.load_map()
        self.reset()

    def load_map(self):
        with open("map.txt", "r") as f:
            for y, line in enumerate(f.readlines()):
                for x, char in enumerate(line.strip()):
                    if char == WALL:
                        self.walls.add((x, y))

    def reset(self):
        self.harry = self.random_position()
        self.cup = self.random_position()
        self.death_eater = self.random_position()
        return self.get_state()

    def random_position(self):
        while True:
            pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if pos not in self.walls:
                return pos

    def render(self):
        self.screen.fill((0, 0, 0))
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)
                if (x, y) in self.walls:
                    pygame.draw.rect(self.screen, (50, 50, 50), rect)
        self.draw_entity(self.cup, (0, 255, 0))
        self.draw_entity(self.harry, (0, 0, 255))
        self.draw_entity(self.death_eater, (255, 0, 0))
        pygame.display.flip()
        self.clock.tick(10)

    def draw_entity(self, pos, color):
        rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, color, rect)

    def step(self, action):
        old_distance = self.manhattan_distance(self.harry, self.death_eater)
        self.harry = self.move(self.harry, action)

        # Death Eater moves
        path = bfs(self.death_eater, self.harry, self.walls, self.width, self.height)
        if len(path) >= 2:
            self.death_eater = path[1]

        new_distance = self.manhattan_distance(self.harry, self.death_eater)

        if self.harry == self.cup:
            return self.get_state(), 1, True
        if self.harry == self.death_eater:
            return self.get_state(), -1, True

        # Encourage staying far from death eater
        reward = -0.01
        if new_distance < old_distance:
            reward -= 0.05  # penalty for getting closer
        else:
            reward += 0.02  # reward for moving away

        return self.get_state(), reward, False

    def manhattan_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def move(self, pos, action):
        x, y = pos
        if action == 0 and y > 0 and (x, y - 1) not in self.walls:
            y -= 1
        elif action == 1 and y < self.height - 1 and (x, y + 1) not in self.walls:
            y += 1
        elif action == 2 and x > 0 and (x - 1, y) not in self.walls:
            x -= 1
        elif action == 3 and x < self.width - 1 and (x + 1, y) not in self.walls:
            x += 1
        return (x, y)

    def get_state(self):
        return (*self.harry, *self.death_eater, *self.cup)
