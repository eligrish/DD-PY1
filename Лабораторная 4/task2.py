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