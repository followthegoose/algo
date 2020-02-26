"""Рекурсивная функция обратного отсчёта"""
def countdown(i):
    print(i)
    if i > 0:
        countdown(i-1)

#countdown(10)

"""Рекурсивная функция вычисления факториала"""
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

#print(fact(3))

"""Рекурсивное вычисление суммы списка"""
def sum(arr):
   if arr == []:
       return 0
   return arr[0] + sum(arr[1:])

#print(sum([1,2,3]))

"""Рекурсивный алгоритм быстрой сортировки"""
def quicksort(arr):
    if len(arr) < 2:                                             #Базовый случай
        return arr
    else:
        center = arr[0]                                          #Опорный элемент
        left = [i for i in arr[1:] if i <= center]               #Все, что меньше опорного элемента
        right = [i for i in arr[1:] if i > center]               #Все, что больше опорного элемента

        return quicksort(left) + [center] + quicksort(right)

print(quicksort([10,5,2,3]))















































