#Задание 1
s = input()

length = len(s)

if length < 5:
    print("Короткая")
elif length <= 10:
    print("Средняя")
else:
    print("Длинная")

#Задание 2
s = input()

if len(s) == 0:
    print("Строка пуста")
else:
    print(s[0], s[-1])

#Задание 3
def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

s = input()

if palindrome(s):
    print("Да")
else:
    print("Нет")

#Задание 4
def contains(s1, s2):
    return s2 in s1

s1 = input()
s2 = input()

if contains(s1, s2):
    print("Да")
else:
    print("Нет")

#Задание 5
def replace_a(s):
    return s.replace("a", "@")

s = input()
print(replace_a(s))

#Задание 6
s = input().split()

surname = s[0].capitalize()
name = s[1][0].upper()
patronymic = s[2][0].upper()

print(surname, name + "." + patronymic + ".")

#Задание 7
s = input()

modified_s = s.replace('а', '')

count_a = len(s) - len(modified_s)

print(count_a)
