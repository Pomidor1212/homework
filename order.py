import letter

# PERSONAL DATA
name = input("Введіть ваше ім'я та прізвище: ")
date = input("Введіть дату поїздки в Карпати: ")
persons = input("Введіть кількість осіб: ")
persons = int(persons)

# PRICE
price_per_person = 15000
total_price = price_per_person * persons
if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0
final_price = total_price - discount

# LETTER
result = letter.LETTER_TEMPLATE.format(
    name=name,
    date=date,
    persons=persons,
    price_per_person=price_per_person,
    total_price=total_price,
    discount=discount,
    final_price=final_price
)
print(result)