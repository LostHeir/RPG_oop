import models
import random
from game_data import enemy_kind, enemy_adjective


class GameLogic:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @staticmethod
    def generate_name():
        return random.choice(enemy_adjective) + ' ' + random.choice(enemy_kind)

    @staticmethod
    def create_character(choice, name):
        return models.Warrior(name=name)

    def spawn_enemy(self):
        return models.Enemy(name=self.generate_name())

