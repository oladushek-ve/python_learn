# - Вам будет дано слово. Ваша задача - вернуть средний символ слова. 
# - Если длина слова нечетная, верните средний символ. 
# - Если длина слова четная, верните средние 2 символа.

def get_middle(s, /):
    str_list = [i for i in s]
    midle_chart = len(str_list) // 2
    if len(str_list) % 2 == 1:
    	return str_list[midle_chart]
    else:
    	return f'{str_list[midle_chart - 1]}{str_list[midle_chart]}'
 #wd green - ssd
print(get_middle('abcdef'))