class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def limited_depth_search(node, goal, limit, depth=0):

    if node is None:
        return None

    print(f"На глубине {depth} проверяем узел {node}")

    # Если найдено значение
    if node.value == goal:
        return node

    if depth >= limit:
        return None


    left_result = limited_depth_search(node.left, goal, limit, depth + 1)
    if left_result:
        return left_result

    right_result = limited_depth_search(node.right, goal, limit, depth + 1)
    return right_result


# Построение дерева из примера
root = BinaryTreeNode(
    1,
    BinaryTreeNode(2, None, BinaryTreeNode(4)),
    BinaryTreeNode(3, BinaryTreeNode(5), None),
)

goal = 4
limit = 2

result = limited_depth_search(root, goal, limit)

# Вывод результата
if result:
    print(f"Цель найдена: {result}")
else:
    print("Цель не найдена в пределах глубины.")
