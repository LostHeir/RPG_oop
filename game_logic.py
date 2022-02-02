import models
import random
from my_utilities import clear
from game_data import enemy_kind, enemy_adjective, logo, game_over


class GameLogic:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @staticmethod
    def print_logo():
        clear()
        print(logo)
        print('Welcome to Debonair Dungeon!')
        input('Press any key to begin..')

    def choose_profession(self):
        print('Who you are?\n'
              '1 - Warrior\n'
              '2 - Mage\n'
              '3 - Rogue')
        try:
            return int(input('I am -> '))
        except ValueError:
            input('You really need to pick one of those options..\n'
                    'Press any key to go back..')

    def chose_action(self):
        clear()
        print('What would You like to do adventurer?\n'
              '1 - I shall introduce myself.\n'
              '2 - I will talk to someone.\n'
              '3 - The whole city must be purged! (Spawns enemy..)')
        try:
            choice = int(input('--> '))
            if 0 >= choice > 3:
                input('You really need to pick one of those options..\n'
                      'Press any key to go back..')
                return None
            return choice

        except ValueError:
            input('You really need to pick one of those options..\n'
                  'Press any key to go back..')

    @staticmethod
    def generate_name() -> str:
        """
        Generates random name for the enemy.
        """
        return random.choice(enemy_adjective) + ' ' + random.choice(enemy_kind)

    @staticmethod
    def create_character(profession: str, name: str) -> models.Hero:
        """
        Creates a hero!
        """
        if profession == 'warrior':
            return models.Warrior(name=name, profession=profession)
        elif profession == 'mage':
            return models.Mage(name=name, profession=profession)
        elif profession == 'rogue':
            return models.Rogue(name=name, profession=profession)

    def spawn_enemy(self) -> models.Enemy:
        """
        Creates a monster.
        """
        return models.Enemy(name=self.generate_name())

    @staticmethod
    def get_skills(profession: models.Hero) -> list:
        """Gets all the skill names for given profession."""
        skills = [method for method in dir(profession) if method.startswith('skill') is True]
        return skills

    @staticmethod
    def print_skills(skills: list):
        """
        Displays skills to the user. Then takes user input as a choice of what to do next.
        """
        i = 1
        print(f'{i} - attack')
        for skill in skills:
            i += 1
            print(f'{i} - {skill}')
        print(f'{i+1} - run')
        try:
            choice = int(input('Next move?: '))
            if 1 > choice or choice > len(skills) + 2:
                input('You really need to pick one of those options..\n'
                      'Press any key to go back..')
                return None
            elif choice == 1:
                return 'attack_enemy'
            elif choice == len(skills) + 2:
                return 'run'
            return skills[choice - 2]
        except ValueError:
            input('You really need to pick one of those options..\n'
                  'Press any key to go back..')
            return None

    def spawn_hero(self, choice):
        if choice and 4 > choice > 0:
            if choice == 1:
                player = self.create_character(profession='warrior', name='LostHeir')
            elif choice == 2:
                player = self.create_character(profession='mage', name='LostHeir')
            elif choice == 3:
                player = self.create_character(profession='rogue', name='LostHeir')
            else:
                raise RuntimeError('Player didnt spawned.')
            return player

    @staticmethod
    def game_over():
        print(game_over)
        input()

