#1st task
try:
    with open('diagnostics.csv', encoding='UTF-8') as file:
        header = file.readline()
        row = file.readline()
    success_open_file = True
except FileNotFoundError:
    success_open_file = False
#2nd task
success_open_file = True
success_file_operations = True
try:
    with open('images/targets.dat', encoding='UTF-8') as f:
        last_row = f.readlines()[-1]
except FileNotFoundError:
    success_open_file = False
except:
    success_file_operations = False
#3d task
try:
    with open('bank.csv', encoding='UTF-8') as f:
        keys = f.readline().strip().split(',')
        values = f.readline().strip().split(',')
        row_data = {}
        for i in range(len(keys)):
            row_data[keys[i]] = values[i]
except FileNotFoundError:
    pass
#4th task
try:
    with open('logs/01-01-2025/log_app.txt', encoding='UTF-8') as f:
        log_errors = []
        for line in f:
            if '[ERROR]' in line:
                log_errors.append(line.strip())
except FileNotFoundError:
    pass
#5th task
try:
    with open('python/course_text.txt', encoding='windows-1251') as f:
        pos = 0
        for line in f:
            line = line.lower()
            if 'python' in line:
                pos+=line.find('python')
                f.seek(pos)
                break
            else:
                pos+=len(line)
except FileNotFoundError:
    pass