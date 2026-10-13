#Задание 1
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")


def main():
    n = int(input())
    multiplication_table(n)


if __name__ == "__main__":
    main()

#Задание 2

def calculate_function():
    x = 0.0

    while x <= 10:
        if x != 5:
            y = (x - 3) / (x - 5)
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