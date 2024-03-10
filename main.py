import sympy as sp
from prettytable import PrettyTable
from sympy import diff

x = sp.Symbol('x')

y = 4*x - sp.cos(x)

# Производные
dy = diff(y, x)
ddy = diff(dy, x)
dddy = diff(ddy, x)

a, b = 0.1, 0.6
x_p = 0.37
h = (b-a)/10

print("\n7 вариант")
print("------------------")
print("Начальные условия:")
print(f"y = {y}")
print(f"[a,b] = [{a}, {b}]")
print(f"x* = {x_p}")
print(f"h = {h}")
print("------------------")


print("\n--- 1 ---\n")


print("Таблица значений функции y=f(x) в равностоящих точках x_i:")
table = PrettyTable(['i', 'x_i', 'f(x_i)'])
values = []
for i in range(11):
    x_i = (a + i*h)
    f_xi = y.evalf(subs={x: x_i})
    values.append([i, x_i.__round__(2), f_xi])
    table.add_row([i, x_i.__round__(2), f_xi.round(2)])

print(table)


print("\n--- 2 ---\n")


x_i = []
f_xi = []
for i in range(len(values)-1):
    if values[i][1] <= x_p <= values[i+1][1]:
        x_i.append(values[i][1])
        x_i.append(values[i+1][1])
        x_i.append(values[i-1][1])
        f_xi.append(values[i][2])
        f_xi.append(values[i+1][2])
        f_xi.append(values[i-1][2])
        break

print(f"x* = {x_p}")
print(f"x_i-1 = {x_i[2]}, x_i = {x_i[0]}, x_i+1 = {x_i[1]}")
print(f"f(x_i-1) = {f_xi[2]}, f(x_i) = {f_xi[0]}, f(x_i+1) = {f_xi[1]}\n")
print("По интерполяционной формуле Лагранжа первого порядка вычислим:")

L1 = f_xi[0] * (x_p - x_i[1])/(x_i[0] - x_i[1]) + f_xi[1] * (x_p - x_i[0])/(x_i[1] - x_i[0])

print(f"L1(x*) = {L1}")


print("\n--- 3 ---\n")


print("С помощью формулы остаточного члена интерполяционной формулы Лагранжа первого порядка найдем:")
R1MaxMin = []
R1MaxMin.append((ddy.evalf(subs={x: x_i[0]}) * (x_p - x_i[0]) * (x_p - x_i[1]) / 2))
R1MaxMin.append((ddy.evalf(subs={x: x_i[1]}) * (x_p - x_i[0]) * (x_p - x_i[1]) / 2))
print(f"R1_min = {min(R1MaxMin)}")

R1_p = y.evalf(subs={x: x_p}) - L1
print(f"R1(x*) = {R1_p}")

print(f"R1_max = {max(R1MaxMin)}")


print("\n--- 4 ---\n")


if min(R1MaxMin) < R1_p < max(R1MaxMin):
    print("Линейная интерполяция, обеспечивающая погрешность, не превосходящую 10^−4: допустима")
    print(f"{min(R1MaxMin)} < {R1_p} < {max(R1MaxMin)}")
else:
    print("Линейная интерполяция, обеспечивающая погрешность, не превосходящую 10^−4: не допустима")


print("\n--- 5 ---\n")


print("С помощью формулы остаточного члена интерполяционной формулы Лагранжа второго порядка вычислим:")

L2 = f_xi[2] * (x_p - x_i[0]) * (x_p - x_i[1]) / ((x_i[2] - x_i[0]) * (x_i[2] - x_i[1])) + f_xi[0] * (x_p - x_i[1]) * (x_p - x_i[2]) / ((x_i[0] - x_i[1]) * (x_i[0] - x_i[2])) + f_xi[1] * (x_p - x_i[2]) * (x_p - x_i[0]) / ((x_i[1] - x_i[2]) * (x_i[1] - x_i[0]))
print(f"L2(x*) = {L2}")


print("\n--- 6 ---\n")


print("С помощью формулы остаточного члена интерполяционной формулы Лагранжа второго порядка найдем:")
R2MaxMin = []
R2MaxMin.append((dddy.evalf(subs={x: x_i[0]}) * (x_p - x_i[0]) * (x_p - x_i[1]) * (x_p - x_i[2]) / 6))
R2MaxMin.append((dddy.evalf(subs={x: x_i[1]}) * (x_p - x_i[0]) * (x_p - x_i[1]) * (x_p - x_i[2]) / 6))
R2MaxMin.append((dddy.evalf(subs={x: x_i[2]}) * (x_p - x_i[0]) * (x_p - x_i[1]) * (x_p - x_i[2]) / 6))
print(f"R2_min = {min(R2MaxMin)}")

R2_p = y.evalf(subs={x: x_p}) - L2
print(f"R2(x*) = {R2_p}")

print(f"R2_max = {max(R2MaxMin)}")


print("\n--- 7 ---\n")


if min(R2MaxMin) < R2_p < max(R2MaxMin):
    print("Квадратичная интерполяция, обеспечивающая погрешность, не превосходящую 10^−5: допустима")
    print(f"{min(R2MaxMin)} < {R2_p} < {max(R2MaxMin)}")
else:
    print("Квадратичная интерполяция, обеспечивающая погрешность, не превосходящую 10^−5: не допустима")


print("\n--- 8 ---\n")


print("Таблица разделенных разностей по узлам x_i−1, x_i, x_i+1:")
table_dif = PrettyTable(['f(x_i−1, x_i, x_i+1)', 'Значение'])
values_2 = []
for i in range(1, len(values)-1):
    f1 = (values[i+1][2] - values[i][2]) / (values[i+1][1] - values[i][1])
    f2 = (values[i][2] - values[i-1][2]) / (values[i][1] - values[i-1][1])
    f = (f1 - f2) / (values[i+1][1] - values[i-1][1])
    table_dif.add_row([f"f({values[i-1][1]}, {values[i][1]}, {values[i+1][1]})", f])
    if values[i][1] == x_i[0]:
        values_2.append(f1)
        values_2.append(f2)
        values_2.append(f)

print(table_dif)

print("\nВычислим интерполяционные многочлены Ньютона:")
L1_n = f_xi[0] + values_2[0] * (x_p - x_i[0])
print(f"L1(x*) = {L1_n}")

L2_n = f_xi[2] + values_2[1] * (x_p - x_i[2]) + values_2[2] * (x_p - x_i[2]) * (x_p - x_i[0])
print(f"L2(x*) = {L2_n}")

print("\nСравнение с соответствующими результатами, полученными по формулам Лагранжа:")
table_comp = PrettyTable(['', 'Лагранж', 'Ньютон'])
table_comp.add_row(['L1', L1, L1_n])
table_comp.add_row(['L2', L2, L2_n])
print(table_comp)