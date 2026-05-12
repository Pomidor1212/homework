from pywebio.input import input, slider
from pywebio.output import put_markdown, put_text

put_markdown("# Планування шкільної поїздки")

students = input("Скільки учнів?", type="number", min=0, value=1)
teachers = input("Скільки вчителів?", type="number", min=0, value=1)

transport = input("Який транспорт? Напиши: Автобус або Поїзд")

days = slider("Скільки днів?", min_value=0, max_value=14, value=1, step=1)

people = students + teachers

if transport == "Автобус":
    buses = people // 40

    if people % 40 != 0:
        buses = buses + 1

    transport_cost = buses * 5000

else:
    buses = 0
    transport_cost = people * 300

hotel_cost = people * 400 * days

total_cost = transport_cost + hotel_cost

discount = 0

if people > 30:
    discount = total_cost * 10 / 100

final_cost = total_cost - discount

put_markdown("## Результат:")

put_text(f"Учнів: {students}")
put_text(f"Вчителів: {teachers}")
put_text(f"Всього людей: {people}")
put_text(f"Транспорт: {transport}")

if transport == "Автобус":
    put_text(f"Потрібно автобусів: {buses}")

put_text(f"Кількість днів: {days}")
put_text(f"Ціна транспорту: {transport_cost} грн")
put_text(f"Ціна проживання: {hotel_cost} грн")
put_text(f"Знижка: {discount} грн")
put_text(f"Фінальна ціна: {final_cost} грн")