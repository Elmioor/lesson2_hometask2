# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# strange_data_list = ['aaa', 0.1, True, 7, 3.14]
# i = 0
# while i < len(strange_data_list):
#     print(type(strange_data_list[i]))
#    i+=1

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

# print("enter data - using space bars  separates elements")
# string_to_parse_on = input()
# print(string_to_parse_on)
# testt_arr = string_to_parse_on.split()
# i=0
# value_to_keep_data =None
# if len(testt_arr) % 2 != 0:
#     print("not even")
#     while i < len(testt_arr) -1:
#         value_to_keep_data = testt_arr[i]
#         testt_arr[i] = testt_arr[i+1]
#         testt_arr[i+1] = value_to_keep_data
#         i += 2
#         print(testt_arr)
# else:
#     while i < len(testt_arr):
#         value_to_keep_data = testt_arr[i]
#         testt_arr[i] = testt_arr[i+1]
#         testt_arr[i+1] = value_to_keep_data
#         i += 2
#         print(testt_arr)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# year_seasons = dict(m_1='winter', m_2='winter', m_3='spring',m_4='spring', m_5='spring', m_6='summer', m_7='summer', m_8='summer', m_9='aurumn', m_10='aurumn', m_11='aurumn', m_12='winter')
# print('enter number 1 <= n <= 12')
# user_input_dtata=int(input())
# month_list_to_search = ['m_1', 'm_2',  'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12']
# print(year_seasons.setdefault(month_list_to_search[user_input_dtata-1]))

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

# print("enter data - using space bars  separates elements")
# string_to_parse_on = input()
# print(string_to_parse_on)
# testt_arr = string_to_parse_on.split()
# i=0
# while i < len(testt_arr):
#     print(i+1, testt_arr[i][0:10])
#     i+=1


## 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
#   result_list.insert(pos, el)	Разместить на позиции pos (индекс элемента списка) элемент el

# my_list = [7, 5, 3, 3, 2]
# print('enter number')
# user_input_dtata=int(input())
# print(max(my_list))
# i=len(my_list)
# while i > 0:
#     if user_input_dtata <=  my_list[i-1]:
#         my_list.insert(i, user_input_dtata)
#         break
#     else:
#         my_list.insert(0, user_input_dtata)
#         break
#     i-=1
# print(my_list)

# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

#**************************************************************************************************
print("how many goods u wanna add?")
goods_number = int(input())
result_arrya_start = []

i = 0
while i < goods_number:
    print("enter next values (!!!SPACES ARE SEPARATORS!!!): \"name\" \"price\" \"ammount\" \"units\"")
    string_to_parse_on = input()
    #print(string_to_parse_on)
    values_string = string_to_parse_on.split()
    result_arrya_start.insert(i, (i+1, {"name":values_string[0], "price": values_string[1], "amm": values_string[2], "unit":values_string[3]}))
    i+=1
print(result_arrya_start)
#**************************************************************************************************

#####****************strange_array= [(1, {'name': '1#$^#^$#^', 'price': '2', 'amm': '33', 'unit': '4'}), (2, {'name': '!!!!2', 'price': '23', 'amm': '44', 'unit': '5'})]
i_i=0

listtt_of_names = []
list_of_prices = []
list_of_amm = []
list_of_units =[]

while i_i < len(result_arrya_start):
    z_list = []
    for el in result_arrya_start[i_i]:
        z_list.append(el)
    i_i+=1
    array_for_values_from_vocabulary_name = z_list[1].get('name')
    array_for_values_from_vocabulary_price = z_list[1].get('price')
    array_for_values_from_vocabulary_amm = z_list[1].get('amm')
    array_for_values_from_vocabulary_unit = z_list[1].get('unit')

    listtt_of_names.append(array_for_values_from_vocabulary_name)
    list_of_prices.append(array_for_values_from_vocabulary_price)
    list_of_amm.append(array_for_values_from_vocabulary_amm)
    list_of_units.append(array_for_values_from_vocabulary_unit)

print(listtt_of_names)
print(list_of_prices)
print(list_of_amm)
print(list_of_units)


resulting_dict = {"name": listtt_of_names,
                  'price': list_of_prices,
                  'amm': list_of_amm,
                  'unit': list_of_units
                  }

print(resulting_dict)
