#                                                   Algo
#                                                        1.Question
# lists = list(input("Enter the circle: ").split(" "))
# a, b, c = lists
# print(" First circle area: ", int(a) ** 2 * 3.14, "\n",
#      "Second circle area: ", int(b) ** 2 * 3.14, "\n",
#      "Third circle area: ", int(c) ** 2 * 3.14, "\n",)

#                                                         2.Question
# year = int(input("Enter the year: "))
# m = 60
# h = m * 60
# d = h * 24
# y = d * 365
# print(f"In {year} years {y* year //1000} litres drop down! ")

#                                                          3.Question
# numbers = int(input("Enter the number: "))
# num = 0
# while numbers > 0:
#    num = num + numbers
#    numbers -= 1
# print("Result: " + str(num))

#                                                           4.Question
# a, b, c = map(int, input("Enter the numbers: ").split(" "))
# if a < b < c:
#    print("Yes")
# else:
#    print("No")

#                                                            5.Question
# a, b, c = map(int, input("Enter the number: ").split(" "))
# if a >= b >= c:
#    print(a * 2, b * 2, c * 2)
# else:
#    print("Wrong numbers")

#                                                             6.Question
# a, b = map(int, input("Enter the numbers: ").split(" "))
# if a > b:
#    print(a)
# else:
#    print(a, b)

#                                                             7.Question
# a, b = map(int, input("Enter the number: ").split(" "))
# if a <= b:
#    a = 0
#    print(a, b)
# else:
#    print(a, b)

#                                                              8.Question
# numbers = list(map(float, input("Enter the numbers: ").split(" ")))
# for i in numbers:
#    if i > 1 and i < 3:
#        print(i)

#                                                               9.Question
# a, b, c = map(int, input("Enter the number: ").split(" "))
# D = (b ** 2 - 4 * c * a)
# if D > 0:
#    x1 = (-b - D ** (1/2)) / (2 * a)
#    x2 = (-b + D ** (1/2)) / (2 * a)
#    print('{:.2f}'.format(x1), '{:.2f}'.format(x2))
# else:
#    print("No real solutions! ")

#                                                               10.Question
# a = int(input("Enter the number: "))
# b = int(input("Enter the second number:"))
# print("Solution is: ", a + b)

#                                                               11.Question
# a = int(input("Enter the number: "))
# b = int(input("Enter the second number: "))
# print("Solution is: ", a * b)

#                                                               12.Question
# a = list(map(int, input("Enter five numbers: ").split(" ")))
# a.sort()
# print(sum(a[:-1]), sum(a[1:]))

#                                                               13.Question
# num = int(input("Enter the amount: "))
# a = list(map(int, input("Enter the numbers: ").split(" ")))
# b = []
# for i in a:
#    if a.count(i) == 1:
#        b.append(i)
# print(b)

#                                                               14.Question
# num = int(input("Enter the amount: "))
# a = list(map(int, input("Enter the numbers: ").split(" ")))
# a.sort()
# print(a[-2])

#                                                               15.Question
# a, b = map(int, input("Enter the numbers: ").split(" "))
# print(b // a)

#                                                               16.Question
# a, b = map(int, input("Enter the numbers: ").split(" "))
# print(b % a)

#                                                               17.Question
# a, b, c = map(int, input("Enter the numbers: ").split(" "))
# if (a + b + c) % 2 != 0:
#    print((a + b + c) // 2 + 1)
# else:
#    print(int((a + b + c) / 2))

#                                                               18.Question
a = int(input("Enter the number: "))




