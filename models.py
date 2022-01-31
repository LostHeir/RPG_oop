import requests
from my_utilities import clear


class Hero:
    def __init__(self, name, profession, strength=0, agility=0, inteligence=0, hp=250, attack=10):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.agility = agility
        self.inteligence = inteligence
        self._attack = attack
        self._profession = profession

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        if strength >= 0:
            self._strength = strength
        else:
            self._strength = 0

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, agility):
        if agility >= 0:
            self._agility = agility
        else:
            self._agility = 0

    @property
    def inteligence(self):
        return self._inteligence

    @inteligence.setter
    def inteligence(self, inteligence):
        if inteligence >= 0:
            self._inteligence = inteligence
        else:
            self._inteligence = 0

    @property
    def profession(self):
        return self._profession

    def introduce(self):
        clear()
        print(f'Sudden spotlight reveals a character..\n'
              f'Hello, I am mighty {self.profession} {self.name}..')
        print(f'{self.name} is flexling..\n'
              f'Current stats:\n'
              f'strength: {self._strength}\n'
              f'agilility: {self._agility}\n'
              f'inteligance: {self._inteligence}\n'
              f'attack points: {self._attack}')


    @staticmethod
    def random_quote():
        try:
            random_quote = requests.get(url="https://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote",
                                        verify=False).json()['content']
        except requests.exceptions.SSLError:
            random_quote = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
                           ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        clear()
        return random_quote

    @property
    def attack(self):
        return self._attack

    def attack_enemy(self, enemy):
        print(f'{self.name} is attacking {enemy.name}.\n{self.name} dealt {self.attack} damage!')
        enemy.hp -= self.attack

    def run(self):
        self.hp -= 10


class Warrior(Hero):
    def __init__(self, armor=0, rage=0, **kwargs):
        super().__init__(**kwargs)
        self.rage = rage
        self._armor = armor

    def introduce(self):
        super().introduce()
        print(f'armor: {self._armor}')
        print(f'rage: {self.rage}')
        input('Press any key to continune..')

    @property
    def rage(self):
        return self._rage

    @rage.setter
    def rage(self, rage):
        if rage >= 0:
            self._rage = rage
        elif rage > 100:
            self._rage = 100
        else:
            self._rage = 0

    @property
    def attack(self, *args, **kwargs):
        return self._attack + 1.25 * self._strength + 0.5 * self._agility

    def rage_management(self, dmg):
        self.rage += dmg
        if dmg == 0:
            self.rage -= 10

    def skill_heroic_strike(self, enemy, *args, **kwargs):
        dmg = self.attack + 0.2 * self._rage
        self.rage_management(dmg=dmg)
        print(f'{self.name} is using heroic strike!.\n{self.name} dealt {dmg} damage!')
        enemy.hp -= dmg

    def skill_shield_wall(self, *args, **kwargs):
        self._armor += 10


class Enemy:
    def __init__(self, name, hp=100, attack=5):
        self.name = name
        self.hp = hp
        self._attack = attack

    @property
    def attack(self):
        return self._attack

    def attack_player(self, player):
        print(f'{self.name} is attacking {player.name}.\n{self.name} dealt {self.attack} damage!')
        player.hp -= self.attack
