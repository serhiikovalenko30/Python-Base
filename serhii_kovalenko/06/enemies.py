class Enemy:
    """
    Class describes enemy
    """
    def __init__(self):

        self._hp = 50
        self._damage = 20

    def attack(self):
        """
        Function to return enemy damage
        """
        return self._damage

    def take_damage(self, damage, race):
        """
        Function to describe fighting
        :param damage: damage from class Character to the enemy
        :param race: class Character who caused damage
        :type damage: int
        :type race: class
        """
        self._hp -= damage
        is_dead = self.is_dead()

        if is_dead:
            print(self.on_death())
            print('You survived. Move on')
        else:
            print(f'Enemy hp: {self._hp}')
            race.on_combat(self)

    def is_dead(self):
        """
        Function to check if char is dead
        """
        if self._hp <= 0:
            return True

    def on_death(self):
        """
        Function returns text on death
        """
        print('I am dead')


class Murloc(Enemy):

    def __init__(self):

        print('I am murloc')
        super().__init__()
        self._hp *= 0.5
        self._damage *= 0.5

    def on_death(self):
        """
        Function returns text on death
        """
        return 'Mrglglglg'


class Undead(Enemy):

    def __init__(self):

        print('I am undead')
        super().__init__()
        self._hp *= 1.2
        self._damage *= 1.1

    def on_death(self):
        """
        Function returns text on death
        """
        return 'Uuuuuh'


# HOMEWORK - new Enemy: Demon and DarkElf
class Demon(Enemy):

    def __init__(self):

        print('I am demon')
        super().__init__()
        self._hp *= 2
        self._damage *= 1.2

    def on_death(self):
        """
        Function returns text on death
        """
        return 'I am immortal'


class DarkElf(Enemy):

    def __init__(self):

        print('I am dark elf')
        super().__init__()
        self._hp *= 0.8
        self._damage *= 0.9

    def on_death(self):
        """
        Function returns text on death
        """
        return 'Good fight'

# HOMEWORK - add new enemy
ENEMIES_TYPES = [Murloc, Undead, Demon, DarkElf]
