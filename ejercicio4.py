class Jedi:
    def __init__(self, name, species, birth_year, lightsaber_color, ranking, masters):
        self.name = name
        self.species = species
        self.birth_year = birth_year
        self.lightsaber_color = lightsaber_color
        self.ranking = ranking
        self.masters = masters

class JediTree:
    def __init__(self):
        self.name_tree = {}
        self.ranking_tree = {}
        self.species_tree = {}

    def add_jedi(self, jedi):
        # Add jedi to name tree
        if jedi.name not in self.name_tree:
            self.name_tree[jedi.name] = jedi

        # Add jedi to ranking tree
        if jedi.ranking not in self.ranking_tree:
            self.ranking_tree[jedi.ranking] = []
        self.ranking_tree[jedi.ranking].append(jedi)

        # Add jedi to species tree
        if jedi.species not in self.species_tree:
            self.species_tree[jedi.species] = []
        self.species_tree[jedi.species].append(jedi)

    def in_order_traversal(self, tree):
        if tree is None:
            return
        self.in_order_traversal(tree.left)
        print(tree.data)
        self.in_order_traversal(tree.right)

    def level_order_traversal(self, tree):
        if tree is None:
            return
        queue = []
        queue.append(tree)
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def get_jedi_info(self, name):
        jedi = self.name_tree.get(name)
        if jedi:
            print(f"Name: {jedi.name}")
            print(f"Species: {jedi.species}")
            print(f"Birth Year: {jedi.birth_year}")
            print(f"Lightsaber Color: {jedi.lightsaber_color}")
            print(f"Ranking: {jedi.ranking}")
            print(f"Masters: {', '.join(jedi.masters)}")

    def get_jedi_by_ranking(self, ranking):
        jedi_list = self.ranking_tree.get(ranking, [])
        for jedi in jedi_list:
            print(jedi.name)

    def get_jedi_by_lightsaber_color(self, color):
        for jedi in self.name_tree.values():
            if jedi.lightsaber_color == color:
                print(jedi.name)

    def get_jedi_with_masters(self):
        for jedi in self.name_tree.values():
            if jedi.masters:
                print(jedi.name)

    def get_jedi_by_species(self, species_list):
        for species in species_list:
            jedi_list = self.species_tree.get(species, [])
            for jedi in jedi_list:
                print(jedi.name)

    def get_jedi_by_name_conditions(self, starts_with, contains):
        for jedi in self.name_tree.values():
            if jedi.name.startswith(starts_with) or contains in jedi.name:
                print(jedi.name)


# Usage example
jedi_tree = JediTree()

# Add Jedi to the tree
jedi_tree.add_jedi(Jedi("Yoda", "Unknown", "896 BBY", "Green", "Jedi Master", []))
jedi_tree.add_jedi(Jedi("Luke Skywalker", "Human", "19 BBY", "Blue", "Jedi Knight", ["Yoda"]))

# Perform in-order traversal by name
print("In-order traversal by name:")
jedi_tree.in_order_traversal(jedi_tree.name_tree)

# Perform in-order traversal by ranking
print("In-order traversal by ranking:")
jedi_tree.in_order_traversal(jedi_tree.ranking_tree)

# Perform level-order traversal by ranking
print("Level-order traversal by ranking:")
jedi_tree.level_order_traversal(jedi_tree.ranking_tree)

# Perform level-order traversal by species
print("Level-order traversal by species:")
jedi_tree.level_order_traversal(jedi_tree.species_tree)

# Get information of Yoda
print("Information of Yoda:")
jedi_tree.get_jedi_info("Yoda")

# Get information of Luke Skywalker
print("Information of Luke Skywalker:")
jedi_tree.get_jedi_info("Luke Skywalker")

# Get Jedi with ranking "Jedi Master"
print("Jedi with ranking 'Jedi Master':")
jedi_tree.get_jedi_by_ranking("Jedi Master")

# Get Jedi with lightsaber color "Green"
print("Jedi with lightsaber color 'Green':")
jedi_tree.get_jedi_by_lightsaber_color("Green")

# Get Jedi with masters
print("Jedi with masters:")
jedi_tree.get_jedi_with_masters()

# Get Jedi of species "Togruta" or "Cerean"
print("Jedi of species 'Togruta' or 'Cerean':")
jedi_tree.get_jedi_by_species(["Togruta", "Cerean"])

# Get Jedi with name starting with "A" or containing "-"
print("Jedi with name starting with 'A' or containing '-':")
jedi_tree.get_jedi_by_name_conditions("A", "-")