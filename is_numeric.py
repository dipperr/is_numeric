def is_numeric(num):
    if num.find(',') != -1:
        lista_bool = []
        lista_nums = num.split(',')
        for i in lista_nums:
            lista_bool.append(True) if i.isnumeric() else lista_bool.append(False)
        if all(lista_bool):
            return True, 'float'
        else:
            return False, None
    elif num.find('.') != -1:
        lista_bool = []
        lista_nums = num.split('.')
        for i in lista_nums:
            lista_bool.append(True) if i.isnumeric() else lista_bool.append(False)
        if all(lista_bool):
            return True, 'float'
        else:
            return False, None
    else:
        if num.isnumeric():
            return True, 'int'
        else:
            return False, None
