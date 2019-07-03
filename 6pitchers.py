# -*- coding: utf-8 -*-

investments = 10
safety = 10
entertainment = 10
needs = 55
gifts = 5
shopping = 10

income = int(input('Введите сумму полученных поступлений --> '))

print('Денежные средства стоит распределить следующим образом:')
print('Инвестиции:', (income/100)*investments)
print('Подушка безопасности:', (income/100)*safety)
print('Отдых и развлечения:', (income/100)*entertainment)
print('Самое необходимое:', (income/100)*needs)
print('Подарки и благотворительность:', (income/100)*gifts)
print('Крупные покупки:', (income/100)*shopping)
