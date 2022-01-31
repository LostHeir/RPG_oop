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
        return models.Warrior(name=name, profession='warrior')

    def spawn_enemy(self):
        return models.Enemy(name=self.generate_name())

    @staticmethod
    def get_skills(profession):
        skills = [method for method in dir(profession) if method.startswith('skill') is True]
        return skills

    @staticmethod
    def print_skills(skills):
        i = 1
        print(f'{i} - attack')
        for skill in skills:
            i += 1
            print(f'{i} - {skill}')
        try:
            choice = int(input('Next move?: '))
            if choice == 1:
                return 'attack_enemy'
            return skills[choice - 2]
        except ValueError:
            input('You really need to pick one of those options..\n'
                  'Press any key to go back..')
            return None

