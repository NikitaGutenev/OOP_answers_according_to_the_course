"""Подвиг 3"""
def input_int_numbers():
    def ex():
        raise TypeError('все числа должны быть целыми')
    value = input()
    return tuple([int(i) if i.isdigit() or i[1:].isdigit() and i[0] == '-' else ex() for i in value.split()])
    
    
while True:
    try:
        res = input_int_numbers()
    except TypeError:
        pass
    else:
        print(*res)
        break


