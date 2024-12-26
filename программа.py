import random

number = random.randint(1, 100)  # Загаданное число
print("Угадайте число от 1 до 100!")
while True:
guess = int(input("Ваш вариант: "))
if guess == number:
print("Поздравляем, вы угадали!")
break
print("Меньше" if guess > number else "Больше")
