def binary_search(list, item):
    low = 0
    hight = len(list)-1

    while low <= hight:
        mid = int((low+hight)/2)
        guess = list[mid]
        print('Может' + str(guess))
        if guess == item:
            return mid
        elif  guess > item:
            hight = mid-1
        else:
            low = mid+1
    return None

my_list = list(range(1,100))
print('Готово! Загаданное число находится на ' + str(binary_search(my_list, 18)) + 'позиции!')