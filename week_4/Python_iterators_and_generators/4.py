def squareatob():
    a = int(input())
    b = int(input())
    sq = (int(i)**2 for i in range(a, b+1))
    for i in range (b - a + 1):
        print(next(sq))
        
squareatob()


"""
Эта функция squareatob() запрашивает у пользователя два целых числа a и b с помощью input(). 
Затем она создает генераторное выражение sq, которое генерирует квадраты чисел от a до b включительно.
Затем функция использует цикл for, который итерируется b - a + 1 раз (чтобы учесть все числа в диапазоне от a до b, включительно).
На каждой итерации из генератора sq извлекается следующее значение с помощью функции next(), а затем это значение (квадрат числа) печатается.
Таким образом, эта функция выводит на экран квадраты всех чисел в диапазоне от a до b включительно.
"""