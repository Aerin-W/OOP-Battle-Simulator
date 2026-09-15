import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.armor = 3


    def attack(self):
        """Return a random amount of damage."""
        doesCriticalHit = random.randint(1,6) == 6
        if doesCriticalHit:
            print(f"{self.name} had a critical hit!")
            return random.randint(2, self.attack_power) + 10
        return random.randint(2, self.attack_power)
        

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        damage = damage - self.armor
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Armor protected health by {self.armor}. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
