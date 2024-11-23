class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def is_path_within_depth(node, goal, limit, depth=0):
    
    if node is None:
        return False

    print(f"На глубине {depth} проверяем комнату {node}")

    # Если найден целевой узел
    if node.value == goal:
        return True

    if depth >= limit:
        return False

    left_result = is_path_within_depth(node.left, goal, limit, depth + 1)
    if left_result:
        return True

    right_result = is_path_within_depth(node.right, goal, limit, depth + 1)
    return right_result


# Построение дерева
root = BinaryTreeNode(
    1,
    BinaryTreeNode(2, None, BinaryTreeNode(4)),
    BinaryTreeNode(3, BinaryTreeNode(5), None),
)

goal = 4 
limit = 2  # Лимит по глубине

found = is_path_within_depth(root, goal, limit)

# Вывод результата
if found:
    print("Найден на глубине: True")
else:
    print("Найден на глубине: False")
