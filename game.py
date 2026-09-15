from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Arena of Fire"
#keep generic
def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage= hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage= enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} wins the battle!")
    else:
        print(f"{enemy} won the battle.")

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
    battle(hero, goblin)



if __name__ == "__main__":
    main()
