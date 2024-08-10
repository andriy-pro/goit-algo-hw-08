import heapq


def minimize_connection_cost(cables):
    # Створюємо "мінімальну купу" з довжинами кабелів
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі є кабелі
    while len(cables) > 1:
        # Витягуємо два найменші
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Обчислюємо витрати на з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо створений кабель назад у чергу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання
cables = [4, 3, 2, 6]  # Довжини кабелів
total_cost = minimize_connection_cost(cables)
print("Загальні витрати на з'єднання кабелів:", total_cost)
