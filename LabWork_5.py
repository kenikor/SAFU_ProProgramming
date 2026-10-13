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