#Задание 1
from itertools import count


def multiplication_table(N):
    for i in range(1,11):
        print(f"{i} x {N} = {i * N}")

def main():
    N = int(input())
    multiplication_table(N)

if __name__ == "__main__":
    main()

#Задание 2
def calculate_function():
    x = 0.0

    while x <= 0:
        if x != 5:
            y = (x-3)/(x-5)
            print(f"x = {x:.1f}, y = {y:.4f}")

        x += 0.5

def main():
    calculate_function()

if __name__ == "__main__":
    main()

#Задание 3
def find_missing(z):
    total = z * (z + 1) // 2

    for i in range(z - 1):
        number = int(input())
        total -= number

    print(total)

def main():
    z = int(input())
    find_missing(z)

if __name__ == "__main__":
    main()

#Задание 4
def input_in_range(a, b):
    while True:
        number = int(input("Введите число \n"))

        if a <= number <= b:
            print("Число корректное")
            break

def main():
    a = int(input())
    b = int(input())
    input_in_range(a, b)

if __name__ == "__main__":
    main()

#Задание 5
import random

def guess_number(a, b):
    secret_number = random.randint(a, b)

    while True:
        number = int(input())

        if number > secret_number:
            print("Перелет")
        elif number < secret_number:
            print("Недолет")
        else:
            print("Число угадано")
            break

def main():
    a = int(input())
    b = int(input())
    guess_number(a, b)

if __name__ == "__main__":
    main()

#Задание 6
def minimum_temperature_days(N):
    minimum = int(input())
    count = 1

    for i in range(N - 1):
        temperture = int(input())

        if temperture < minimum:
            minimum = temperture
            count = 1
        else:
            count += 1

    print(count)

def main():
    N = int(input())
    minimum_temperature_days(N)

if __name__ == "__main__":
    main()

#Задание 7
def NOD_function(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a

def NOD_recursive(a, b):
    if a == b:
        return a

    if a > b:
        return NOD_recursive(a - b, b)

    return NOD_recursive(a, b - a)

def main():
    a = int(input())
    b = int(input())

    print(NOD_function(a, b))
    print(NOD_recursive(a, b))

if __name__ == "__main__":
    main()

#Задание 8
def factorial_for(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_while(n):
    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1

    return result


def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


def main():
    n = int(input())

    print(factorial_for(n))
    print(factorial_while(n))
    print(factorial_recursive(n))


if __name__ == "__main__":
    main()

#Задание 10
def calculate_money(N):
    nomination = 64

    while nomination >= 1:
        count = N // nomination

        if count > 0:
            print(nomination, "-", count)

        N %= nomination
        nomination //= 2

def main():
    N = int(input())
    calculate_money(N)

if __name__ == "__main__":
    main()