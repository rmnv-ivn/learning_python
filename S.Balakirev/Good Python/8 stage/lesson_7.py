#1st task
msg = input()

with open('letter.txt', 'w', encoding='UTF-8') as f:
    f.write(msg)
#2nd task
msg = input()

with open('work_data/log_stats.txt', 'a+', encoding='UTF-8') as f:
    f.write(msg)
    f.seek(0)
    header = f.readline()
#3d task
try:
    with open('lib/text_1', encoding='UTF-8') as f:
        f.readline()
        file1 = f.read()
    with open('lib/text_2', encoding='UTF-8') as f:
        f.readline()
        file2 = f.read()
    with open('text_all.txt', 'w', encoding='Windows-1251') as f:
        f.writelines([file1 + '\n', file2])
except FileNotFoundError:
    pass
#4th task
try:
    with open('lang_doc/python_base.dat', encoding='UTF-8') as f:
        python = f.read()
    with open('lang_doc/java_base.dat', encoding='UTF-8') as f:
        java = f.read()
    with open('lang_doc/python_base.dat', 'w', encoding='UTF-8') as f:
        f.write(java)
    with open('lang_doc/java_base.dat', 'w', encoding='UTF-8') as f:
        f.write(python)
except FileNotFoundError:
    pass