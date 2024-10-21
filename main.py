input_file = open('text.txt', 'r') #Открываем файл для чтения
output_file = open('output.txt', 'w') #Открываем файл для записи
line_number = 1 #Инициализируем счетчик строк
for line in input_file: #Читаем строки из входного файла
    output_file.write(f"{line_number}: {line}") #Записываем номер строки и саму строку в выходной файл
    line_number += 1  #Увеличиваем счетчик строк
input_file.close() #Закрываем файл
output_file.close() #Закрываем файл
