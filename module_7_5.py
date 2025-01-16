import os
import time

print('Текущая директория:',os.getcwd())
directory = r'C:\Users\Татьяна\PycharmProjects\PythonProject\7'

for root, dirs, files in os.walk(directory):

    for file in files:
# Примените os.path.join для формирования полного пути к файлам.
        filepath = os.path.join(root, file)
#Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#Используйте os.path.getsize для получения размера файла
        file_size = os.path.getsize(filepath)
#Используйте os.path.dirname для получения родительской директории файла.
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')