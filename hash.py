import numpy as np
import re

#таблица перестановок
#делаем таким образом таблицу со случаными числами
num_e = [5,9,1,4,5,2,3,5,3,6,8,2,8,7,4,7,1,3,5,2] #взяты из числа е
table_perm = []
def table_permutation(nums):
    table_perm.append(num_e)
    for i in range(1, 20):
        table_perm.append(list(np.random.permutation(table_perm[i-1])))
    return table_perm


perm = table_permutation(num_e)


#получение значения для каждого элемента
def hash(string,count=0):
    sum = 0
    for pos in range(len(string)):        
        sum = sum + ord(string[pos])*perm[count][pos%20] #формула 
    return (sum//len(string))%512


filename = "hash_text.txt"
with open(filename, encoding="utf8") as file:
    text =re.sub('\n',' ',(re.sub(r'[^\w\s]','', file.read()))).split(' ') #очистка текста от мусора
    

#если какой-то элемент получает в результате функции hash число, которым уже было зашифровано значение
#оно перехешируется с помощью drop_repeat
def drop_repeat(table, word):
    c = 0
    h = hash(word)
    while h in list(hashe_table.values()):
        h = hash(word,c)
        c+=1
    return c

#вывод хэш-таблицы
def hash_table_out(table):
    for x, value in table.items():
        print(x,': ',value)
        print('')
        





#процесс записи хэш таблицы
hashe_table = {}
for word in text:
    if word not in hashe_table:
        if hash(word) not in list(hashe_table.values()):
            hashe_table[word] = hash(word)
        else:
            hashe_table[word] = hash(word, drop_repeat(hashe_table, word))

  
        
