class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def find_max_at_depth(root, limit):
   
    if root is None:
        return None

    # Очередь для BFS
    queue = [(root, 0)]
    max_value = float('-inf')
    found = False

    while queue:
        current_node, depth = queue.pop(0)

        if depth > limit:
            break

        if depth == limit:
            max_value = max(max_value, current_node.value)
            found = True

        if current_node.left:
            queue.append((current_node.left, depth + 1))
        if current_node.right:
            queue.append((current_node.right, depth + 1))

    return max_value if found else None


# Построение дерева
root = BinaryTreeNode(
    3,
    BinaryTreeNode(1, BinaryTreeNode(0), None),
    BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
)

limit = 2

# Запуск функции
result = find_max_at_depth(root, limit)

# Вывод
if result is not None:
    print(f"Максимальное значение на указанной глубине: {result}")
else:
    print("Узлы на указанной глубине отсутствуют.")
