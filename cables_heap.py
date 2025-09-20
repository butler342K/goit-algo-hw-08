import heapq

# Функція для обчислення мінімальних витрат на з’єднання кабелів
def min_cost_cables(cables):
    heapq.heapify(cables)  # створюємо мінімальну купу
    total_cost = 0
    steps = []

    while len(cables) > 1:
        # витягуємо два найкоротші кабелі
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        # з’єднуємо їх
        cost = a + b
        total_cost += cost
        # зберігаємо крок з’єднання
        steps.append((a, b, cost))
        # повертаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost, steps


