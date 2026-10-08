# Задание 1
A = float(input())
B = float(input())
C = float(input())

if A >= B and A >= C:
    maximum = A
elif B >= A and B >= C:
    maximum = B
else:
    maximum = C

if A <= B and A <= C:
    minimum = A
elif B <= A and B <= C:
    minimum = B
else:
    minimum = C

print(maximum, minimum)

# Задание 2
import math
a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Бесконечно много корней")
        else:
            print("Корней нет")
    else:
        x = -c / b
        print(x)
else:
    D = b * b - 4 * a * c

    if D < 0:
        print("Корней нет")
    elif D == 0:
        x = -b / (2 * a)
        print(x)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(x1, x2)

# Залание 3
A = float(input())
B = float(input())
C = float(input())

if A <= 0 or B <= 0 or C <= 0:
    print("Нет")
elif A + B <= C or A + C <= B or B + C <= A:
    print("Нет")
else:
    print("Да")

    if A == B and B == C:
        print("Равносторонний")
    elif A == B or A == C or B == C:
        print("Равнобедренный")
    else:
        print("Разносторонний")

#Задание 4
x = float(input())
y = float(input())

if x * x + y * y <= 1:
    print("Yes")
elif x <= 0 and y <= 0 and x + y >= -2:
    print("Yes")
else:
    print("No")

# Задание 5
M = int(input())
D = int(input())

if M < 1 or M > 12:
    print(-1)
elif M == 2 and (D < 1 or D > 28):
    print(-1)
elif M == 4 or M == 6 or M == 9 or M == 11:
    if D < 1 or D > 30:
        print(-1)
    else:
        print((30 - D) + (12 - M) * 30)
elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
    if D < 1 or D > 31:
        print(-1)
    else:
        days = 0

        if M == 1:
            days = 334 + (31 - D)
        elif M == 3:
            days = 275 + (31 - D)
        elif M == 5:
            days = 214 + (31 - D)
        elif M == 7:
            days = 153 + (31 - D)
        elif M == 8:
            days = 123 + (31 - D)
        elif M == 10:
            days = 62 + (31 - D)
        elif M == 12:
            days = 31 - D

        print(days)
else:
    if D < 1 or D > 31:
        print(-1)

# Задание 6
K = int(input())

if K < 0:
    print("Мы не находили грибы, а только теряли")
elif K % 10 == 1 and K % 100 != 11:
    print("Мы нашли в лесу", K, "гриб")
elif (K % 10 == 2 or K % 10 == 3 or K % 10 == 4) and not (K % 100 == 12 or K % 100 == 13 or K % 100 == 14):
    print("Мы нашли в лесу", K, "гриба")
else:
    print("Мы нашли в лесу", K, "грибов")

# Задание 7
t = int(input())

if t % 5 < 3:
    print("Зеленый")
else:
    print("Красный")

#Задание 8
y = int(input())

hours = y // 30
minutes = (y % 30) * 2

print(hours, minutes)