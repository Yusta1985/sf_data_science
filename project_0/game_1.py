import numpy as np
number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
def random_predict(number) -> int:
    """Компьютер угадывает рандомное число

    Args:
        number (int, optional): Загаданное число.
        
    Returns:
        int: Число попыток
    """
    
    count = 0
    min = 1
    max = 100
    
    # number = np.random.randint(1, 101)
    print(number)
    while True:
        count += 1
        md = round((min + max)/2)
        print(md)
        if md > number:
            max = md
        elif md < number:
            min = md
        else:
            print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break # конец игры и выход из цикла
        
    return(count)

print(f'Количество попыток: {random_predict(number)}')
