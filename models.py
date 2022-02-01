"""Cointains all models of heroes and monsters."""

import requests
from my_utilities import clear


class Hero:
    """
    Base class for future heroes.
    """
    def __init__(self, name: str, profession: str, strength=0, agility=0, inteligence=0, hp=250, attack=10):
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
    def strength(self, strength: int):
        if strength >= 0:
            self._strength = strength
        else:
            self._strength = 0

    @property
    def agility(self) -> int:
        return self._agility

    @agility.setter
    def agility(self, agility: int):
        if agility >= 0:
            self._agility = agility
        else:
            self._agility = 0

    @property
    def inteligence(self) -> int:
        return self._inteligence

    @inteligence.setter
    def inteligence(self, inteligence: int):
        if inteligence >= 0:
            self._inteligence = inteligence
        else:
            self._inteligence = 0

    @property
    def profession(self) -> str:
        return self._profession

    def introduce(self):
        """
        One of basic hero actions. Hero introduce himself and shows his attributes.
        """
        clear()
        print(f'Sudden spotlight reveals a character..\n'
              f'Hello, I am mighty {self.profession} {self.name}..')
        print(f'{self.name} is flexling..\n'
              f'Current stats:\n'
              f'strength: {self._strength}\n'
              f'agility: {self._agility}\n'
              f'inteligance: {self._inteligence}\n'
              f'attack points: {self._attack}')

    @staticmethod
    def random_quote() -> str:
        """
        One of basic hero actions. Hero simulates talking with a NPC, and get random response.
        Apparently all NPC are from Star Wars universe.

        Method uses swquotes API to get random quote from Star Wars universe.
        API doesn't have valid certificates.
        In case of SSLError replace quote with Lorem ipsum placeholder.
        :return: quote as string
        """
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

    def attack_enemy(self, enemy: 'Enemy'):
        """
        One of bacis hero actions. Hero attacks enemy.
        """
        print(f'{self.name} is attacking {enemy.name}.\n{self.name} dealt {self.attack} damage!')
        enemy.hp -= self.attack

    def run(self, *args, **kwargs):
        """
        One of bacis hero actions. Runs from enemy losing some hp.
        """
        self.hp -= 10


class Enemy:
    """
    Basic class of enemy. In future different types of enemies can have different attributes.
    """
    def __init__(self, name: str, hp=100, attack=5):
        self.name = name
        self.hp = hp
        self._attack = attack

    @property
    def attack(self):
        return self._attack

    def attack_player(self, player: Hero):
        print(f'{self.name} is attacking {player.name}.\n{self.name} dealt {self.attack} damage!')
        player.hp -= self.attack


class Warrior(Hero):
    """
    One of possible hero professions. Have 2 additional skills:
    Heroic Strike - Enchants attacks with rage.
    Shield Wall - Increases armor.
    :param rage: Enchants attacks, raises when dealing dmg, decreases over time.
    :param armor: Reduces enemy attacks.
    """
    def __init__(self, armor=0, rage=0, **kwargs):
        super().__init__(**kwargs)
        self.rage = rage
        self._armor = armor

    def introduce(self):
        """
        Overrides basic method.
        Adds more description of hero profession.
        """
        super().introduce()
        print(f'armor: {self._armor}')
        print(f'rage: {self.rage}')
        input('Press any key to continune..')

    @property
    def rage(self):
        return self._rage

    @rage.setter
    def rage(self, rage: float):
        if rage >= 0:
            self._rage = rage
        elif rage > 100:
            self._rage = 100
        else:
            self._rage = 0

    @property
    def attack(self, *args, **kwargs):
        return self._attack + 1.25 * self._strength + 0.5 * self._agility

    def rage_management(self, dmg: float):
        """
        Enchants attacks, raises when dealing dmg, decreases over time.
        """
        self.rage += dmg
        if dmg == 0:
            self.rage -= 10

    def skill_heroic_strike(self, enemy: Enemy, *args, **kwargs):
        """
        Enchants attacks with rage.
        """
        dmg = self.attack + 0.2 * self._rage
        self.rage_management(dmg=dmg)
        print(f'{self.name} is using heroic strike!.\n{self.name} dealt {round(dmg,2)} damage!')
        enemy.hp -= dmg

    def skill_shield_wall(self, *args, **kwargs):
        """
        Reduces enemy attacks.
        """
        self._armor += 10


class Mage(Hero):
    """
    One of possible hero professions. Have 2 additional skills:
    Cone of Ice - Attacks enemy with ice, using mana.
    Meditate - Increases mana.
    :param crit_chance: Increases dmg of the attacks and skills.
    :param mana: Basic resource of this profession. Used to cast spells.
    """
    def __init__(self, mana=100, crit_chance=0, **kwargs):
        super().__init__(**kwargs)
        self.inteligence = 5
        self.mana = mana
        self._crit_chance = crit_chance

    def introduce(self):
        """
        Overrides basic method.
        Adds more description of hero profession.
        """
        super().introduce()
        print(f'crit_chance: {self._crit_chance}')
        print(f'mana: {self.mana}')
        input('Press any key to continune..')

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana: float):
        if mana >= 0:
            self._mana = mana
        elif mana > 100:
            self._mana = 100
        else:
            self._mana = 0

    @property
    def attack(self, *args, **kwargs):
        return self._attack + 0.25 * self.strength + 0.5 * self.agility + 1.25 * self.inteligence

    def skill_cone_of_ice(self, enemy: Enemy, *args, **kwargs):
        """
        Attacks enemy with ice, using mana.
        """
        if self.mana < 30:
            print("Not enough mana!")
            return None
        dmg = self.attack + 3.5 * self.inteligence
        print(f'{self.name} is using cone of ice!.\n{self.name} dealt {round(dmg,2)} damage!')
        self.mana -= 30
        enemy.hp -= dmg

    def skill_meditate(self, *args, **kwargs):
        """
        Increases mana.
        """
        self.mana += 50


class Rogue(Hero):
    """
    One of possible hero professions. Have 2 additional skills:
    Backstab - Attacks from behind uses energy.
    Sharp weapons - Increases energy.
    :param crit_chance: Increases dmg of the attacks and skills.
    :param energy: Basic resource of this profession. Used to cast spells.
    """
    def __init__(self, energy=100, crit_chance=0, **kwargs):
        super().__init__(**kwargs)
        self.agility = 5
        self.energy = energy
        self._crit_chance = crit_chance

    def introduce(self):
        """
        Overrides basic method.
        Adds more description of hero profession.
        """
        super().introduce()
        print(f'crit_chance: {self._crit_chance}')
        print(f'energy: {self.energy}')
        input('Press any key to continune..')

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy: float):
        if energy >= 0:
            self._energy = energy
        elif energy > 100:
            self._energy = 100
        else:
            self._energy = 0

    @property
    def attack(self, *args, **kwargs):
        return self._attack + 0.75 * self.strength + 1.5 * self.agility + 0.25 * self.inteligence

    def skill_backstab(self, enemy: Enemy, *args, **kwargs):
        """
        Attacks enemy from behind!
        """
        if self.energy < 30:
            print("Not enough energy!")
            return None
        dmg = self.attack + 1.5 * self.inteligence
        print(f'{self.name} is using cone of ice!.\n{self.name} dealt {round(dmg,2)} damage!')
        self.energy -= 15
        enemy.hp -= dmg

    def skill_sharp_weapons(self, *args, **kwargs):
        """
        Increases energy.
        """
        self.energy += 50




