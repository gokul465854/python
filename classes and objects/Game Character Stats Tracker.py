class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"\n{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (
            f"\nName   : {self.name}\n"
            f"Level  : {self.level}\n"
            f"Health : {self.health}\n"
            f"Mana   : {self.mana}"
        )


# ---------------- MAIN PROGRAM ----------------

name = input("Enter character name: ")

hero = GameCharacter(name)

print("\n=== Character Created ===")
print(hero)

damage = int(input("\nEnter damage taken: "))
hero.health -= damage

mana_used = int(input("Enter mana used: "))
hero.mana -= mana_used

print("\n=== Updated Character Stats ===")
print(hero)

choice = input("\nLevel up character? (yes/no): ").lower()

if choice == "yes":
    hero.level_up()
    print("\n=== Character After Level Up ===")
    print(hero)