'''
Object class for a character
TODO:
    1. Classes / Crew Position
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
    def __init__(self, name, health, strength, defense, stamina, level, experience, berries, bounty, statpoints, moves=None, items=None):
        self._name = name
        self._health = health
        self._strength = strength
        self._defense = defense
        self._stamina = stamina
        self._level = level
        self._experience = experience
        self._berries = berries
        self._statpoints = statpoints
        self._bounty = bounty
        self._moves = moves if moves else []
        self._items = items if items else []

        # stats dictionary
        self.stats = {
            "Name": self.name,
            "Health": self.health,
            "Strength": self.strength,
            "Defense": self.defense,
            "Stamina": self.stamina,
            "Level": self.level,
            "Experience": self.experience,
            "Berries": self.berries,
            "Bounty": self.bounty,
            "Stat Points": self.statpoints,
            "Moves": self.moves,
            "Items": self.items
        }

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
    def bounty(self):
        return self._bounty
        
    @property
    def statpoints(self):
        return self._statpoints
    
    @property
    def moves(self):
        return self._moves
    
    @property
    def items(self):
        return self._items

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

    @bounty.setter
    def bounty(self, bounty):
        self._bounty = bounty

    @statpoints.setter
    def statpoints(self, statpoints):
        self._statpoints = statpoints

    @moves.setter
    def moves(self, moves):
        self._moves = moves

    @items.setter
    def items(self, items):
        self._items = items

    '''
    Add move
    '''
    def learn_move(self, move):
        self.moves.append(move)

    '''
    Add item
    '''
    def add_item(self, item):
        self.items.append(item)

    '''
    Take damage
    '''
    def take_damage(self, damage):
        self.health -= damage

    '''
    Prints character's stats
    Able to choose which stats to display
    '''
    def print_stats(self, display_stats=None):
        if display_stats is None:
            display_stats = self.stats.keys()

        print(f"\n{self.name}'s stats:")
        for key in display_stats:
            if key in self.stats:
                if key == "Moves":
                    if len(self.stats[key]) == 0:
                        print(f"{key}: None")
                        continue
                    move_names = [move.name for move in self.stats[key]]
                    print(f"{key}: {', '.join(move_names)}")
                elif key == "Items":
                    if len(self.stats[key]) == 0:
                        print(f"{key}: None")
                        continue
                    item_names = [item.name for item in self.stats[key]]
                    print(f"{key}: {', '.join(item_names)}")
                else:    
                    print(f"{key}: {self.stats[key]}")

    '''
    Updates a character's stats
    '''
    def update_stat(self, stat_name, value):
        if stat_name in self.stats:
            setattr(self, stat_name.lower(), value)
            self.stats[stat_name] = value

    '''
    CURRENTLY IN PROGRESS
    Allow user to upgrade their stats
    '''
    def upgrade_stats(self):
        upgradeable_stats = [key for key in self.stats if key not in ["Name", "Level", "Experience", "Berries", "Stat Points"]]


        if self.statpoints <= 0:
            print("\nERROR: You have no stat points to allocate to your stats!")
            return
        while(self.statpoints > 0 ):
            print(f"\nYou have {self.statpoints} stat points to allocate.")
        
            print("\nSelect which stat you would like to upgrade")
            print("0. Exit")
            for i, stat in enumerate(upgradeable_stats, 1):
                print(f"{i}. {stat}")

            try:
                choice = int(input("> "))

                if choice == 0:
                    print("Exiting stat upgrade.")
                    break

                if 1 <= choice <= len(upgradeable_stats):
                    selected_stat = upgradeable_stats[choice - 1]
                    quantity = int(input(f"How many points would you like to add to {selected_stat}: "))

                    if quantity <= 0:
                        print("ERROR: Enter a positive integer!")
                        continue
                        
                    if quantity > self.statpoints:
                        print("ERROR: Not enough stat points available!")
                        continue

                    new_value = self.stats[selected_stat] + quantity
                    self.update_stat(selected_stat, new_value)
                    self.statpoints -= quantity
                    print(f"\nSUCCESS: {selected_stat} increased to {self.stats[selected_stat]}!")
                else:
                    print("ERROR: Invalid choice!")
            except ValueError: 
                print("ERROR: Enter a number!")
        print("SUCCESS: Stat upgrade(s) complete!")

        
    '''
    CURRENTLY IN PROGRESS
    Allow user to create a character
    Make them allocate their stat points
    '''
    def character_creation(self):
        print("Create Your Character")

        name = input("Enter your character name: ")

        character = Character(name, 10, 10, 10, 10, 1, 0, 0, 0, 10, [], [])

        character.print_stats(["Health", "Strength", "Defense", "Stamina"])

        character.upgrade_stats()

        character.print_stats()

'''
Object class for an Enemy
TODO:
    1. Different types of enemies
'''
class Enemy:
    def __init__(self, name, health, strength, defense, stamina, level, berries, moves, items):
        self._name = name
        self._health = health
        self._strength = strength
        self._defense = defense
        self._stamina = stamina
        self._level = level
        self._berries = berries
        self._moves = moves
        self._items = items

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
    def berries(self):
        return self._berries
    
    @property
    def moves(self):
        return self._moves
    
    @property
    def items(self):
        return self._items
    
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
        
    @berries.setter
    def berries(self, berries):
        self._berries = berries

    @moves.setter
    def moves(self, moves):
        self._moves = moves
    
    @items.setter
    def moves(self, items):
        self._items = items
        

'''
Object class for Moves
'''
class Move:
    def __init__(self, name, damage, stamina, description):
        self.name = name
        self.damage = damage
        self.stamina = stamina
        self.description = description

    def __repr__(self):
        return f"Move('{self.name}')"
    
    def use(self, target):
        target.take_damage(self.damage)

'''
Object class for Items
'''
class Item:
    def __init__(self, name, type, effect, description):
        self._name = name
        self._type = type
        self._effect = effect
        self._description = description

'''
Starting a new game will make you create a character and play the game
TODO:
    1. Levels
    2. Combat
'''
def start():
    print("\n*************************\n")
    print("Starting Game")
    print("\n*************************\n")

    user = Character("", 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [])
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
    print("\n*************************\n")
    print("!Welcome to Rogue Piece!")
    print("\n*************************\n")

    while True:
        print("Select an option")
        print("0. Exit Game")
        print("1. Start Game")
        print("2. Load Game")
        print("3. How To Play")

        try:
            choice = int(input("> "))

            if choice == 0:
                print("Exiting")
                break
            elif choice == 1:
                start()
                break
            elif choice == 2:
                load()
                break
            elif choice == 3:
                how_to_play()
                break
            else:
                print("ERROR: Enter a valid choice!")
        except ValueError:
            print("ERROR: Enter a number!")
    
if __name__ == "__main__":
    main()

'''
Test for adding moves
print("Testing Game\n")

    punch = Move("Punch", 5, 1, "A simple punch")
    kick = Move("Kick", 10, 2, "A simple kick")

    user = Character("Dummy", 10, 10, 10, 10, 1, 0, 0, 0, 10, [], [])

    print("Before adding Moves")
    user.print_stats()

    user.learn_move(punch)
    user.learn_move(kick)

    print("\nAfter adding Moves")
    user.print_stats()
'''