#Задание 1
A = int(input())
B = int(input())
N = int(input())

cake = (A * 100 + B)* N

rub = cake // 100
cop =  cake % 100

#Задание 2
print(rub, cop)

N = int(input())

print(N % 2 == 0)

#Задание 3
N = int(input())
K = int(input())

nuts = K // N
prize = K % N

print(nuts, prize)

#Задание 4
a = int(input())

hundreds = a // 100
tens = a // 10 % 10
units = a % 10

summ = hundreds + tens + units
comp = hundreds * tens * units

print(summ, comp)

#Задание 5
A = int(input())
B = int(input())
C = int(input())

desk_A = (A + 1) // 2
desk_B = (B + 1) // 2
desk_C = (C + 1) // 2

summ = desk_A + desk_B + desk_C

print(summ)

#Задание 6
A = int(input())
B = int(input())
L = int(input())
N = int(input())

length = A * (2 * N - 1) + 2 * B * (N - 1) + 2 *L

print(length)

#Задание 7
h = int(input())
m = int(input())
s = int(input())
h1 = int(input())
m1 = int(input())
s1 = int(input())

start = h * 3600 + m * 60 + s
end = h1 * 3600 + m1 * 60 + s1

difference =  end - start

H = difference // 3600
M = difference % 3600 // 60
S = difference % 60

print(H, "ч", M, "м", S, "с")