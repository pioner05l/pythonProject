
# # f = open('example.txt', 'r')
# f = open('example.txt', 'r', encoding='utf-8')
# print(f)
# print(*f)
# f.close()


# f = open('example.txt', 'r')
# try:
#     print(*f)
# finally:
#     f.close()


# with open('example.txt', 'r') as f:
#     print(*f)


# with open('example.txt', 'r') as f:
#     s = f.read()
# print(s, type(s))


# with open('example.txt', 'r') as f:
#     print(f.readline())
#     print(f.readline())


# with open('example.txt', 'r') as f:
#     s = f.readline()
# s_n = []
# for i in s:
#     i = i.replace('\n', '')
#     s_n.append(i)
# print(s_n)


# with open('example.txt', 'w') as f:
#     f.write('Hello \nWorld')


import os
# # os.rename('example.txt', 'ex_2.txt')
# print('Текущая дериктория:', os.getcwd())


# os. mkdir('folder') # Создание папки

# os.chdir('folder')
# print('Текущая дериктория:', os.getcwd())
#
# with open('test.txt', 'w') as f:
#     f.write('Hello')


# os.chdir('folder')
# print('Текущая дериктория:', os.getcwd())
# os.chdir('..')
# print('Текущая дериктория:', os.getcwd())
# os.makedirs('n1/n2/n3')


# os.remove('folder/test.txt') # удоление файлов

# os.rmdir('folder') # Удоление папки

# os.removedirs('n1/n2/n3') # Удоление котологов


# В файле, в одну строку записаны слова и числа через пробел или _ найти
# сумму всех чисел.

# with open('task_1.txt') as f:
#     s = f.read()
#     print(s)
#
# s = s.replace('_', ' ')
# a = s.split()
# print(a)
# s = 0
# for i in a:
#     if i.isdigit():
#         i = int(i)
#         s += i
# print(s)