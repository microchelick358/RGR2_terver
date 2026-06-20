import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
lam = 73          # Среднее количество вызовов (лямбда)
days = 365        # Количество дней для симуляции

# 1. Генерируем случайное количество вызовов для каждого из 365 дней
# Согласно распределению Пуассона
calls_per_day = np.random.poisson(lam, days)

# 2. Вычисляем кумулятивное среднее (среднее значение по мере накопления дней)
# То есть среднее за 1 день, за 2 дня, за 3 дня и т.д.
cumulative_days = np.arange(1, days + 1)
cumulative_average = np.cumsum(calls_per_day) / cumulative_days

# 3. Визуализация
plt.figure(figsize=(12, 6))
plt.plot(cumulative_days, cumulative_average, label='Среднее значение в симуляции', color='blue')
plt.axhline(y=lam, color='red', linestyle='--', label=f'Теоретическое среднее (λ={lam})')

plt.title('Иллюстрация Закона Больших Чисел (ЗБЧ)')
plt.xlabel('Количество дней (n)')
plt.ylabel('Среднее число вызовов')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Вывод итогового результата
print(f"Среднее количество вызовов за {days} дней: {cumulative_average[-1]:.2f}")