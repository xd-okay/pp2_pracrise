# def square_generator(n):
#     """Генератор квадратов чисел от 0 до n-1"""
#     for i in range(n):
#         yield i ** 2

# # Использование генератора
# n_limit = 6
# squares = square_generator(n_limit)

# print(f"Квадраты чисел до {n_limit}:")
# for sq in squares:
#     print(sq)

#2
# def even(k):
#     for i in range(k+1):
#         if(i%2==0):
#             yield str(i)
            


# a=int(input())
# even_num=even(a)
# for im in even_num:
#     print(even_num)
#3
# def divisible_by_3_and_4(n):
#     for i in range(n + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# # Тест
# n = int(input("Введите предел n: "))
# for num in divisible_by_3_and_4(n):
#     print(num)

# #4
# def squares(a, b):
#     for i in range(a, b + 1):
#         yield i ** 2

# # Тест с циклом for
# start, end = 2, 6
# print(f"Квадраты от {start} до {end}:")
# for sq in squares(start, end):
#     print(sq)

# 5
# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# # Или через range:
# # def countdown(n):
# #     for i in range(n, -1, -1):
# #         yield i

# # Тест
# n_val = 5
# print(f"Обратный отсчет от {n_val}:")
# for num in countdown(n_val):
#     print(num)