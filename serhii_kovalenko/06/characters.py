class Character:
    """
    Class describes character
    """
    def __init__(self, name):
        """
        :param name: name char
        :type name: str
        """
        self.name = name
        self._hp = 100
        self._damage = 10

    def is_dead(self):
        """
        Function to check if char is dead
        """
        if self._hp <= 0:
            return True

    def on_combat(self, enemy):
        """
        Function to describe fighting
        :param enemy: enemy from class Enemy
        :type enemy: class
        """
        self._hp -= enemy.attack()
        is_dead = self.is_dead()

        if is_dead:
            return print('Game over')

        print(f'Char hp: {self._hp}')
        enemy.take_damage(self._damage, self)

# HOMEWORK - new Function: hill and move
    def hill(self):
        """
        Function to describe life replenishment
        """
        hp_before = self._hp
        self._hp += 10
        return print(f'Your HP = {hp_before}. You found a bottle of life and your hp = {self._hp}')

    def move(self):
        """
        Function to describe move
        """
        return input('Travel. Please choose where to go (u, d, l, r): ')


class Orc(Character):
    """
    Class to describe Orc race
    """
    def __init__(self, name):
        """
        :param name: name char
        :type name: str
        """
        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.5
        self._damage *= 1.2


# HOMEWORK - new Race
class Elf(Character):
    """
    Class to describe Elf race
    """
    def __init__(self, name):
        """
        :param name: name char
        :type name: str
        """
        super().__init__(name)  # call to Character().__init__

        self._hp *= 0.8
        self._damage *= 0.9


# HOMEWORK - add new Race
# races to be checked within a game loop.
RACES = {'orc': Orc, 'elf': Elf}
