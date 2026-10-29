#1st task
f_log = open('log.dat', encoding='utf-8')
lines = f_log.readlines()
header = lines[0]
last_data = lines[-1]
f_log.close()
#2nd task
f_inp = open('sites/links.txt', encoding='windows-1251')
f_inp.read()
size_file = f_inp.tell()
f_inp.close()
#3d task
f_text = open('course.new.dat', encoding='UTF-8')
start_5 = f_text.read(5)
f_text.read()
end_pos = f_text.tell()
f_text.seek(end_pos-5, 0)
end_5 = f_text.read()
f_text.close()
#4th task
fp = open('projects/python/works.my', encoding='UTF-8')
fragment = fp.read()[9:20]
fp.close()
#5th task
fp = open('staff/persons.dat', encoding='UTF-8')
num_person = 0
for i,line in enumerate(fp):
    person = line.strip()
    name = line.split()[0]
    lname = line.split()[2]
    if name=='Сергей' and lname=='Балакирев':
        num_person = i+1
fp.close()