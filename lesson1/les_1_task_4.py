# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

a = ord('a')
letter1 = input('Введите первую букву >>> ')
letter2 = input('Введите вторую букву >>> ')
pos1 = ord(letter1) - a + 1
pos2 = ord(letter2) - a + 1
if pos1 == pos2:
    dif = 0
else:
    dif = abs(pos2 - pos1 - 1)
print(f'Перва буква находится на месте номер: {pos1}, вторая буква на месте: {pos2}. Между ними находится {dif} букв')