# Модуль 7.5: Файлы в операционной системе

Создайте новый проект или продолжите работу в текущем проекте.

Используйте функцию os.walk для обхода каталога, путь к которому хранится в переменной directory.
С помощью os.path.join сформируйте полный путь к файлам.
Воспользуйтесь os.path.getmtime и модулем time, чтобы получить и отобразить время последнего изменения файла.
Для получения размера файла используйте os.path.getsize().
Чтобы узнать родительскую директорию файла, воспользуйтесь os.path.dirname().

### Комментарии к заданию:

Ключевая идея — использование вложенного цикла for.

```python
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath =?
    filetime =?
    formatted_time = time.strftime("%d.%m.%Y%H:%M", time.localtime(filetime))
    filesize =?
    parent_dir =?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
```

Поскольку в разных операционных системах схема расположения папок может отличаться, проще всего тестировать в папке проекта, установив переменную directory в значение «.».

### Пример возможного вывода:

```
Обнаружен файл: main.py, Путь:./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория:.
```

