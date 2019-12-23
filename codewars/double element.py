# Получив массив целых чисел, верните новый массив с каждым удвоенным значением.

def maps(a):
    #if list have 1 element or more, then do element*2
    if len(str(a)) > 0:
        double_list = [i * 2 for i in a]
        return double_list
    #else return empty list
    else:
        return a