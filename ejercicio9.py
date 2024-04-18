class Character:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

class IndexTree:
    def __init__(self):
        self.root = None

    def add_character(self, character):
        # Add character to the index tree
        pass

    def modify_character(self, name, new_character):
        # Modify character in the index tree
        pass

    def remove_character(self, name):
        # Remove character from the index tree
        pass

    def get_character_info(self, name):
        # Get information of a specific character
        pass

    def get_yoda_info(self):
        # Get information of Yoda
        pass

    def get_boba_fett_info(self):
        # Get information of Boba Fett
        pass

    def get_tall_characters(self):
        # Get a sorted list of characters taller than 1 meter
        pass

    def get_light_characters(self):
        # Get a sorted list of characters weighing less than 75 kilos
        pass

# Usage example
index_tree = IndexTree()

# Add characters to the index tree
character1 = Character("Luke Skywalker", 1.72, 77)
index_tree.add_character(character1)

character2 = Character("Yoda", 0.66, 13)
index_tree.add_character(character2)

character3 = Character("Boba Fett", 1.83, 78)
index_tree.add_character(character3)

# Modify a character
new_character = Character("Luke Skywalker", 1.75, 80)
index_tree.modify_character("Luke Skywalker", new_character)

# Remove a character
index_tree.remove_character("Luke Skywalker")

# Get information of Yoda and Boba Fett
yoda_info = index_tree.get_yoda_info()
boba_fett_info = index_tree.get_boba_fett_info()

# Get a sorted list of characters taller than 1 meter
tall_characters = index_tree.get_tall_characters()

# Get a sorted list of characters weighing less than 75 kilos
light_characters = index_tree.get_light_characters()