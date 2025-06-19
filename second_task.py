import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок
N = 100000

# Метод Монте-Карло
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
monte_carlo_integral = (b - a) * np.mean(y_random)

# Аналітичне значення
analytical_value, _ = quad(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_integral:.6f}")
print(f"Аналітичне значення (quad): {analytical_value:.6f}")
print(f"Абсолютна похибка: {abs(monte_carlo_integral - analytical_value):.6f}")

# --- Побудова графіка ---
x_vals = np.linspace(-0.5, 2.5, 400)
y_vals = f(x_vals)

fig, ax = plt.subplots()
# Малювання функції
ax.plot(x_vals, y_vals, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3, label="Площа під кривою")

# Налаштування графіка
ax.set_xlim([x_vals[0], x_vals[-1]])
ax.set_ylim([0, max(y_vals) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Інтегрування f(x) = x² від 0 до 2")
ax.legend()
plt.grid()
plt.show()
