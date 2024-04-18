class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_binary_tree(levels):
    if levels == 0:
        return None

    root = Node(levels)
    root.left = generate_binary_tree(levels - 1)
    root.right = generate_binary_tree(levels - 1)

    return root

def cut_tree_levels(root, levels):
    if levels == 0:
        return None

    if root is None:
        return None

    root.left = cut_tree_levels(root.left, levels - 1)
    root.right = cut_tree_levels(root.right, levels - 1)

    return root

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)

def pre_order_traversal(root):
    if root is None:
        return

    print(root.value)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

def find_tree_with_most_nodes(trees):
    max_nodes = 0
    max_tree = None

    for tree in trees:
        nodes = count_nodes(tree)
        if nodes > max_nodes:
            max_nodes = nodes
            max_tree = tree

    return max_tree

def is_tree_complete(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_tree_complete(root.left) and is_tree_complete(root.right)

    return False

# Generar el árbol binario con nueve niveles
tree = generate_binary_tree(9)

# Cortar los tres primeros niveles del árbol
forest = []
for i in range(3):
    cut_tree = cut_tree_levels(tree, i)
    forest.append(cut_tree)

# Contar cuántos nodos tiene cada árbol del bosque
node_counts = []
for tree in forest:
    node_count = count_nodes(tree)
    node_counts.append(node_count)

# Realizar un barrido preorden de cada árbol del bosque
for tree in forest:
    pre_order_traversal(tree)

# Determinar cuál es el árbol con mayor cantidad de nodos
max_tree = find_tree_with_most_nodes(forest)

# Indicar qué árboles del bosque están completos
complete_trees = []
for tree in forest:
    if is_tree_complete(tree):
        complete_trees.append(tree)