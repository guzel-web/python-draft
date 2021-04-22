import os.path

os.chdir('main')  # Изменить директорию
# os.chdir('sample')
print(os.getcwd())
print()
lst = []
for current_dir, dirs, files in os.walk('.'):
    if files is not None:
        for i in files:
            if i[-3::] == '.py':
                lst.append(current_dir)
                break
lst.sort()
f = open('test1', 'w')
for j in lst:
    if j[0:2:] == '.\\':
        f.writelines('main\\' + j[2::] + '\n')
    elif j[0:1:] == '.':
        f.writelines('main' + j[1::] + '\n')
f.close()
