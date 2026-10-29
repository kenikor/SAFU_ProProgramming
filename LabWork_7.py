

import random

# 1

def create_list_1(n):
    return list(range(n))


def create_list_2(n):
    return [random.randint(1, 100) for _ in range(n)]


def create_list_3(n):
    return list(map(int, input().split()))


n = int(input())
print(create_list_1(n))


# 2

def task_2(lst):
    print(lst[:3])
    print(lst[-1])
    print(lst[1:5])
    print(sum(lst[1:9]))


lst = list(range(1, 11))
task_2(lst)


# 3

def task_3(lst, k1, k2):
    return lst[k2:] + lst[k1:k2] + lst[:k1]


lst = [1, 2, 3, 4, 5, 6, 7, 8]
k1 = int(input())
k2 = int(input())
print(task_3(lst, k1, k2))


# 4

def task_4_1(n):
    return [i * 11 for i in range(1, n + 1)]


def task_4_2(lst):
    return [x for sublist in lst for x in sublist]


def task_4_3(n):
    return [[i, i * 10] for i in range(1, n + 1)]


def task_4_4():
    return [i ** 2 if i % 2 == 0 else i + 2 for i in range(1, 21)]


n = int(input())
print(task_4_1(n))
print(task_4_2([[1, 10], [2, 20], [3, 30], [4, 40]]))

if n <= 9:
    print(task_4_3(n))

print(task_4_4())


# 5

def task_5(n):
    lst = [random.randint(1, 10) for _ in range(n)]

    print(lst)
    print(min(lst))
    print(lst.index(min(lst)))
    print(max(lst))
    print(lst.index(max(lst)))
    print(len(lst))

    for x in dict.fromkeys(lst):
        print(x, lst.count(x))


n = int(input())
if n > 0:
    task_5(n)


# 6

def task_6():
    lst = input().split()

    lst.sort()
    print("***".join(lst))

    lst.sort(reverse=True)
    print("+++".join(lst))


task_6()


# 7

def task_7(names, math, russian, informatics):
    students = []

    for i in range(len(names)):
        total = math[i] + russian[i] + informatics[i]
        students.append([i, names[i], total])

    students.sort(key=lambda x: x[2], reverse=True)

    for student in students[:10]:
        print(f"{student[0]}: {student[1]}")


names = [
    "Иванов Иван Иванович",
    "Петров Пётр Петрович",
    "Сидоров Алексей Сергеевич",
    "Смирнова Анна Ивановна",
    "Кузнецов Дмитрий Олегович",
    "Попова Мария Андреевна",
    "Васильев Артём Игоревич",
    "Соколова Елена Дмитриевна",
    "Михайлов Кирилл Павлович",
    "Фёдорова Ольга Сергеевна",
    "Новиков Максим Евгеньевич",
    "Морозова Дарья Алексеевна",
    "Волков Никита Романович",
    "Алексеева София Денисовна",
    "Лебедев Андрей Михайлович"
]

math = [90, 75, 88, 95, 70, 92, 81, 85, 78, 96, 89, 83, 72, 94, 80]
russian = [85, 80, 90, 91, 76, 88, 84, 87, 79, 93, 86, 82, 75, 90, 81]
informatics = [95, 70, 92, 89, 74, 90, 88, 91, 77, 98, 93, 85, 78, 96, 83]

task_7(names, math, russian, informatics)
