class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.append(Node(char))
        elif char in operators:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack.pop()

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def evaluate_expression(node):
    if node.value.isdigit():
        return int(node.value)

    left_val = evaluate_expression(node.left)
    right_val = evaluate_expression(node.right)

    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

expression = input("Enter a mathematical expression: ")
root = build_expression_tree(expression)

print("Inorder traversal:")
inorder_traversal(root)

print("\nResult:", evaluate_expression(root))