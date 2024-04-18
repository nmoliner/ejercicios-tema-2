class Node:
    def __init__(self, name, is_hero):
        self.name = name
        self.is_hero = is_hero
        self.left = None
        self.right = None

def insert(root, name, is_hero):
    if root is None:
        return Node(name, is_hero)
    if name < root.name:
        root.left = insert(root.left, name, is_hero)
    elif name > root.name:
        root.right = insert(root.right, name, is_hero)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        if not root.is_hero:
            print(root.name)
        in_order_traversal(root.right)

def starts_with_C(root):
    if root:
        starts_with_C(root.left)
        if root.name.startswith('C'):
            print(root.name)
        starts_with_C(root.right)

def count_superheroes(root):
    if root is None:
        return 0
    return count_superheroes(root.left) + count_superheroes(root.right) + (1 if root.is_hero else 0)

def find_and_modify(root, target_name, new_name):
    if root:
        if root.name == target_name:
            root.name = new_name
        else:
            find_and_modify(root.left, target_name, new_name)
            find_and_modify(root.right, target_name, new_name)

def reverse_order_traversal(root):
    if root:
        reverse_order_traversal(root.right)
        print(root.name)
        reverse_order_traversal(root.left)

# Create the tree
root = None
root = insert(root, "Iron Man", True)
root = insert(root, "Captain America", True)
root = insert(root, "Thor", True)
root = insert(root, "Hulk", True)
root = insert(root, "Black Widow", True)
root = insert(root, "Loki", False)
root = insert(root, "Thanos", False)
root = insert(root, "Ultron", False)
root = insert(root, "Doctor Strange", True)

# List villains alphabetically
print("Villains:")
in_order_traversal(root)

# List superheroes starting with C
print("Superheroes starting with C:")
starts_with_C(root)

# Count superheroes
num_superheroes = count_superheroes(root)
print("Number of superheroes:", num_superheroes)

# Find and modify Doctor Strange's name
find_and_modify(root, "Doctor Strange", "Dr. Strange")

# List superheroes in reverse order
print("Superheroes in reverse order:")
reverse_order_traversal(root)

class Forest:
    def __init__(self):
        self.hero_tree = None
        self.villain_tree = None

    def insert_hero(self, name):
        self.hero_tree = self._insert(self.hero_tree, name, True)

    def insert_villain(self, name):
        self.villain_tree = self._insert(self.villain_tree, name, False)

    def _insert(self, root, name, is_hero):
        if root is None:
            return Node(name, is_hero)
        if name < root.name:
            root.left = self._insert(root.left, name, is_hero)
        elif name > root.name:
            root.right = self._insert(root.right, name, is_hero)
        return root

    def count_nodes(self, root):
        if root is None:
            return 0
        return self.count_nodes(root.left) + self.count_nodes(root.right) + 1

    def alphabetical_traversal(self, root):
        if root:
            self.alphabetical_traversal(root.left)
            print(root.name)
            self.alphabetical_traversal(root.right)

# Create the forest
forest = Forest()
forest.insert_hero("Iron Man")
forest.insert_hero("Captain America")
forest.insert_hero("Thor")
forest.insert_hero("Hulk")
forest.insert_hero("Black Widow")
forest.insert_villain("Loki")
forest.insert_villain("Thanos")
forest.insert_villain("Ultron")

# Determine the number of nodes in each tree
num_hero_nodes = forest.count_nodes(forest.hero_tree)
num_villain_nodes = forest.count_nodes(forest.villain_tree)
print("Number of nodes in hero tree:", num_hero_nodes)
print("Number of nodes in villain tree:", num_villain_nodes)

# Alphabetical traversal of hero tree
print("Hero tree traversal:")
forest.alphabetical_traversal(forest.hero_tree)

# Alphabetical traversal of villain tree
print("Villain tree traversal:")
forest.alphabetical_traversal(forest.villain_tree)