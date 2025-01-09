'''
Object for a character
TODO:
    1. Classes / Crew Posititon
        - Fighter
            - Fighting styles
        - Sniper
            - Ranged weapons
        - Navigator
            - Choose what island to go to
        - Doctor
            - Heals
    2. Devil Fruits
    3. Races
        - Minks
        - Giants
    3. Inventory
    endurance, strength, health, agility
'''
class Character:
    def __init__(self, name, health, strength, defense, stamina, level, experience, berries, statpoints):
        self._name = name
        self._health = health
        self._strength = strength
        self._defense = defense
        self._stamina = stamina
        self._level = level
        self._experience = experience
        self._berries = berries
        self._statpoints = statpoints

    # Getters
    @property
    def name(self):
        return self._name
        
    @property
    def health(self):
        return self._health
        
    @property
    def strength(self):
        return self._strength
        
    @property
    def defense(self):
        return self._defense
        
    @property
    def stamina(self):
        return self._stamina
        
    @property
    def level(self):
        return self._level
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def berries(self):
        return self._berries
        
    @property
    def statpoints(self):
        return self._statpoints

    # Setters
    @name.setter
    def name(self, name):
        self._name = name

    @health.setter
    def health(self, health):
        self._health = health

    @strength.setter
    def strength(self, strength):
        self._strength = strength
        
    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @stamina.setter
    def stamina(self, stamina):
        self._stamina = stamina

    @level.setter
    def level(self, level):
        self._level = level

    @experience.setter
    def experience(self, experience):
        self._experience = experience
        
    @berries.setter
    def berries(self, berries):
        self._berries = berries

    @statpoints.setter
    def statpoints(self, statpoints):
        self._statpoints = statpoints

    def print_stats(self, display_stats=None):
        stats = {
            "Name": self.name,
            "Health": self.health,
            "Strength": self.strength,
            "Defense": self.defense,
            "Stamina": self.stamina,
            "Level": self.level,
            "Experience": self.experience,
            "Berries": self.berries,
            "Stat Points": self.statpoints,
        }

        if display_stats is None:
            display_stats = stats.keys()

        print(f"{self.name}'s stats:")
        for key in display_stats:
            if key in stats:
                print(f"{key}: {stats[key]}")

    def add_stats(self, stat_points):
        self.statpoints = stat_points

        print(f"You have {stat_points} stat points to allocate to your stats")

        while(stat_points > 0):
            try:
                add_health = int(input("Enter how many stat points to add to Health: "))

                stat_points -= add_health

            except ValueError:
                print("ERROR: Please enter ")
    
    def character_creation(self):
        print("Create Your Character")

        name = input("Enter your character name: ")

        character = Character(name, 10, 10, 10, 10, 1, 0, 0, 10)

        character.print_stats(["Health", "Strength", "Defense", "Stamina"])

        character.add_stats(character.statpoints)

        character.print_stats()
        
'''
Starting a new game will make you create a character and play the game
TODO:
    1. Levels
    2. Combat
'''
def start():
    print("Starting Game")

    user = Character("", 0, 0, 0, 0, 0, 0, 0, 0)
    user.character_creation()

'''
Load Game Saves
TODO:
    1. Ways to save game?
        - json
'''
def load():
    print("Load Game")

'''
Gives instructions on how to play
TODO:
    1. Create instructions
'''
def how_to_play():
    print("Instruction ")


def main():
    print("Welcome to One Piece Roguelike")

    while True:
        print("Select an option")
        print("0. Exit Game")
        print("1. Start Game")
        print("2. Load Game")
        print("3. How To Play")

        try:
            choice = int(input("> "))

            match choice:
                case 0:
                    print("Exiting")
                    break
                case 1:
                    start()
                    break
                case 2:
                    load()
                    break
                case 3:
                    how_to_play()
                    break
                case _:
                    print("ERROR: Enter a valid choice!")
        except ValueError:
            print("ERROR: Enter a number!")

if __name__ == "__main__":
    main()