# Поиск с ограничением глубины по личному графу
from collections import deque

# Граф с расстояниями между городами
graph = {
    "Стамбул": [("Бурса", 155), ("Эскишехир", 480), ("Анкара", 450)],
    "Бурса": [("Стамбул", 155), ("Анкара", 480), ("Маниса", 70)],
    "Эскишехир": [("Стамбул", 480), ("Анкара", 230)],
    "Анкара": [("Эскишехир", 230), ("Стамбул", 450), ("Бурса", 480), ("Сивас", 320), ("Конья", 260)],
    "Маниса": [("Бурса", 70), ("Измир", 330)],
    "Измир": [("Маниса", 330), ("Анталья", 460)],
    "Конья": [("Анкара", 260), ("Анталья", 290), ("Мерсин", 460)],
    "Анталья": [("Измир", 460), ("Конья", 290)],
    "Мерсин": [("Конья", 460), ("Адана", 70)],
    "Адана": [("Мерсин", 70), ("Газантеп", 220)],
    "Газантеп": [("Адана", 220), ("Шанлыурфа", 150)],
    "Шанлыурфа": [("Газантеп", 150), ("Диярбакыр", 180)],
    "Диярбакыр": [("Шанлыурфа", 180), ("Ван", 320)],
    "Ван": [("Диярбакыр", 320), ("Эрзурум", 370)],
    "Эрзурум": [("Ван", 370), ("Трабзон", 250)],
    "Трабзон": [("Эрзурум", 250), ("Самсун", 330)],
    "Самсун": [("Трабзон", 330), ("Сивас", 410)],
    "Сивас": [("Самсун", 410), ("Анкара", 320), ("Кайсери", 240)],
    "Кайсери": [("Сивас", 240), ("Малатья", 240)],
    "Малатья": [("Кайсери", 240), ("Шанлыурфа", 90)]
}

# Алгоритм поиска с ограничением глубины
def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, depth):
        if node == goal:
            return (True, depth)
        if depth == limit:
            return (False, float('inf'))  # Ограничение
        min_distance = float('inf')
        for neighbor, distance in graph.get(node, []):
            found, dist = recursive_dls(neighbor, depth + 1)
            if found:
                return (True, dist + distance)
            min_distance = min(min_distance, dist)
        return (False, min_distance)

    found, result = recursive_dls(start, 0)
    return result if found else None

# Проверка
start = "Стамбул"
goal = "Анкара"
limit = 3
result = depth_limited_search(graph, start, goal, limit)
print(f"Минимальное расстояние: {result}" if result else "Решение не найдено")
