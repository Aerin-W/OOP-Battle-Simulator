from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Arena of Fire"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Jribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Peanut")
    
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")
    
    hero = Hero("Mrs. Bryan")

    print(f"{hero.name} enters the arena with {hero.health} health. Hero has {hero.armor} armor points.")


    heroattacknum = hero.attack()

    goblin.take_damage(heroattacknum)

    goblinattacknum= goblin.attack()

    hero.take_damage(goblinattacknum)




if __name__ == "__main__":
    main()
