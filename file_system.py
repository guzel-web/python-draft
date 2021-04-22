import os
import os.path
# import shutil
# shutil.copy('', '') #копирование файла
# shutil.copytree('', '')

print(os.getcwd()) # показывает текущую директорию
print()
print(os.listdir()) # распечатывает, что содержится в текущей директории
print()
print(os.path.exists('test.txt')) # Существует ли данная папка(либо директория) в текущей директории
print()
print(os.path.isdir('test.txt')) # Эта директория?
print(os.path.isdir('.idea')) # Эта директория?
print()
print(os.path.isfile('test.txt')) # Это файл?
print(os.path.isfile('.idea'))  # Это файл?
print()
print(os.path.abspath('test.txt')) # Абсолютный путь до файла
print()
# os.chdir('.idea') # Изменить директорию
# print(os.getcwd())
print()
for current_dir, dirs, files in os.walk('.'):
    # os.walk('.') позволяет рекурсивно пройтись по всем папкам папкамкам и т.д.,
    # в возврашает генератор, когда спрашиваем следующее значение,
    # возвращает кортеж из 3х элементов:
    # строковое представление текущей директорииБ которое осматривает
    # список из всех подпапок, которые есть в данной директории
    # список всех файлов которые есть в данной директории
    print(current_dir, dirs, files)