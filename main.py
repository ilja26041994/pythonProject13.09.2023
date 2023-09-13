# # Есть лестница, состоящая из n ступенек.
# # Вы можете за один шаг подниматься на 1 или на 2 ступеньки. Напишите функцию climbStairs(),
# # которая бы подсчитывала количество всех возможных вариантов подняться на эту лестницу.
# #
# # Примеры работы данной функции:
# # climbStairs(5) —> 8
# # climbStairs(8) —> 34
# # climbStairs(35) —> 14930352
# import funktion
# try:
#     nomberOfStairs = int(input('Введите количество ступенек: '))
# except Exception as e:
#     print(e)
# n = nomberOfStairs
# listOfStairs = []
# for i in range(n):
#     listOfStairs.append(i)
# print(listOfStairs)
# print(funktion.climbStairs(n))


# # Напишите функцию, которая будет принимать координаты двух точек на плоскости и возвращать длину отрезка,
# # соединяющего эти точки. Порядок передаваемых чисел — X, Y. Результат нужно округлить до сотых.
# #
# # Примеры:
# # line_length([15, 7], [22, 11]) ➞ 8.06
# # line_length([0, 0], [0, 0]) ➞ 0
# # line_length([0, 0], [1, 1]) ➞ 1.41
#
# def line_length(x, y):
#     return round(((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5, 2)
#
# print(line_length([15, 7], [22, 11]))
# print(line_length([0, 0], [0, 0]))
# print(line_length([0, 0], [1, 1]))
