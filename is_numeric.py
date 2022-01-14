def is_numeric(num):
    if num.find(',') != -1:
        lista_bool = []
        lista_nums = num.split(',')
        for i in lista_nums:
            lista_bool.append(True) if i.isnumeric() else lista_bool.append(False)
        return all(lista_bool)
    elif num.find('.') != -1:
        lista_bool = []
        lista_nums = num.split('.')
        for i in lista_nums:
            if i.isnumeric():
                lista_bool.append(True)
            else:
                lista_bool.append(False)
        return all(lista_bool)
    else:
        return num.isnumeric()
