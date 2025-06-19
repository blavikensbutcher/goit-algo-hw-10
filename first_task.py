import pulp


model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)


lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat="Integer")


model += lemonade + fruit_juice, "Total_Production"


model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_limit"
model += 1 * lemonade <= 50, "Sugar_limit"
model += 1 * lemonade <= 30, "Lemon_juice_limit"
model += 2 * fruit_juice <= 40, "Fruit_puree_limit"


model.solve()


print("Статус розв'язання:", pulp.LpStatus[model.status])
print("Кількість виробленого Лимонаду:", int(lemonade.varValue))
print("Кількість виробленого Фруктового соку:", int(fruit_juice.varValue))
print("Загальна кількість напоїв:", int(pulp.value(model.objective)))
