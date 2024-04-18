class Node:
    def __init__(self, name, defeated_by=None, description=None, captured=None):
        self.name = name
        self.defeated_by = defeated_by
        self.description = description
        self.captured = captured
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.name > node.name:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        defeated_by = " and ".join(node.defeated_by) if node.defeated_by else "None"
        print(f"{node.name}: defeated by {defeated_by}")
        inorder_traversal(node.right)

def search(node, name):
    if node is None or node.name == name:
        return node
    if node.name < name:
        return search(node.right, name)
    return search(node.left, name)

def update_captured(node, name):
    if node:
        update_captured(node.left, name)
        if node.name in name:
            node.captured = name
        update_captured(node.right, name)

def delete(node, name):
    if node is None:
        return node
    if name < node.name:
        node.left = delete(node.left, name)
    elif name > node.name:
        node.right = delete(node.right, name)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        node.name = find_min(node.right).name
        node.right = delete(node.right, node.name)
    return node

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def level_order_traversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.name)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Create the tree
root = Node("Talos", defeated_by=["Jason"], description="A giant bronze automaton")
insert(root, Node("Cerbero", defeated_by=["Heracles"], description="A three-headed dog guarding the gates of the Underworld"))
insert(root, Node("Toro de Creta", defeated_by=["Heracles"], description="A monstrous bull"))
insert(root, Node("Cierva Cerinea", defeated_by=["Heracles"], description="A sacred deer"))
insert(root, Node("Jabalí de Erimanto", defeated_by=["Heracles"], description="A giant boar"))
insert(root, Node("Basilisco", defeated_by=["Unknown"], description="A venomous serpent with a deadly gaze"))
insert(root, Node("Sirenas", defeated_by=["Unknown"], description="Enchanting creatures that lure sailors with their songs"))
insert(root, Node("Aves del Estínfalo", defeated_by=["Unknown"], description="Birds with sharp metallic feathers"))
insert(root, Node("Ladón", defeated_by=["Unknown"], description="A hundred-headed dragon guarding the golden apples"))
insert(root, Node("Medusa", defeated_by=["Perseus"], description="A gorgon with snakes for hair"))
insert(root, Node("Minotauro", defeated_by=["Theseus"], description="A half-man, half-bull creature"))
insert(root, Node("Quimera", defeated_by=["Bellerophon"], description="A fire-breathing monster with the body of a lion, the head of a goat, and the tail of a serpent"))
insert(root, Node("Hidra de Lerna", defeated_by=["Heracles"], description="A serpent-like water monster with multiple heads"))
insert(root, Node("Cíclope", defeated_by=["Odysseus"], description="A one-eyed giant"))
insert(root, Node("Pegaso", defeated_by=["Bellerophon"], description="A winged horse"))
insert(root, Node("Grifo", defeated_by=["Unknown"], description="A creature with the body of a lion and the head of an eagle"))

# Perform queries
print("Inorder traversal:")
inorder_traversal(root)

print("\nDescription of Talos:")
talos = search(root, "Talos")
if talos:
    print(f"Name: {talos.name}")
    print(f"Defeated by: {', '.join(talos.defeated_by)}")
    print(f"Description: {talos.description}")
    print(f"Captured by: {talos.captured}")

print("\nTop 3 heroes/demigods with most defeated creatures:")
heroes = {}
def count_defeated(node):
    if node:
        count_defeated(node.left)
        if node.defeated_by:
            for hero in node.defeated_by:
                heroes[hero] = heroes.get(hero, 0) + 1
        count_defeated(node.right)
count_defeated(root)
top_heroes = sorted(heroes.items(), key=lambda x: x[1], reverse=True)[:3]
for hero, count in top_heroes:
    print(f"{hero}: {count} defeated creatures")

print("\nCreatures defeated by Heracles:")
heracles = search(root, "Heracles")
if heracles:
    inorder_traversal(heracles)

print("\nCreatures not defeated:")
defeated_creatures = set()
def get_defeated_creatures(node):
    if node:
        get_defeated_creatures(node.left)
        if node.defeated_by:
            defeated_creatures.add(node.name)
        get_defeated_creatures(node.right)
get_defeated_creatures(root)
not_defeated_creatures = [node.name for node in level_order_traversal(root) if node.name not in defeated_creatures]
print(not_defeated_creatures)

print("\nUpdating captured creatures:")
update_captured(root, "Heracles")
inorder_traversal(root)

print("\nDeleting Basilisco and Sirenas:")
root = delete(root, "Basilisco")
root = delete(root, "Sirenas")
inorder_traversal(root)

print("\nUpdating Aves del Estínfalo:")
aves = search(root, "Aves del Estínfalo")
if aves:
    aves.defeated_by.append("Heracles")
inorder_traversal(root)

print("\nUpdating Ladón:")
ladon = search(root, "Ladón")
if ladon:
    ladon.name = "Dragón Ladón"
inorder_traversal(root)

print("\nLevel order traversal:")
level_order_traversal(root)
