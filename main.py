# "1st program"
print(9**0.5*5)

# "2nd program"
print(9.99>9.98 and 1000!=1000.1)

# "3rd program"

number1 = 1234

# Удаляем последнюю цифру числа 1234
number = number1 // 10  # Получаем 123

# Удаляем первую цифру из оставшегося числа 123
result1 = number % 100  # Получаем 23

number2 = 5678

# Удаляем последнюю цифру числа 5678
number = number2 // 10  # Получаем 567

# Удаляем первую цифру из оставшегося числа 567
result2= number % 100  # Получаем 67

print(result1+result2)


# "4th program"
a, b = 13.42, 42.13

ai, bi = int(a), int(b)
af, bf = int((a - ai) * 100), int((b - bi) * 100)
print(ai == bf or bi == af)