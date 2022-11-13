def get_count_char(str_):  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    dict_amount = {}
    for letter in str_:
         alpha = letter.isalpha()
         if alpha == True:
             letter_amount = str_.count(letter)
             dict_amount[letter] = letter_amount
    return dict_amount
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_percent_char(dictionary):

    """Функция, которая принимает словарь с буквами
        в качестве ключа и количеством букв в качестве
        значений и возвращает новый словарь, где количество
        каждого элемента заменено на процентное отношение
        ко всем символам"""

    dictionary_percent_symbols = {}
    values = dictionary.values()
    sum_values = sum(values)
    for key in dictionary:
        dictionary_percent_symbols[key] = dictionary_symbols[key] * 100 / sum_values

    return dictionary_percent_symbols

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

dictionary_symbols = get_count_char(main_str)

print(get_count_char(main_str))
print(get_percent_char(dictionary_symbols))
