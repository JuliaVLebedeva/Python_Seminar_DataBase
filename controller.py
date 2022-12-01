from student_database import save_db, load_db
from teacher import add_student, put_rating
from student import see_rating

def controller():
    load_db()     #выгрузка данных из файлf DB_student.json
    match input('укажите себя. 1 - учитель 2 - ученик: '):
        # блок кода учителя
        case '1':
            flag = 1
            while flag == 1:
                print('Что хотите сделать?')
                act = input('1 - запись ученика 2 - выставить оценку, 0 - выйти из программы\nВвод: ')
                if act == '1':
                    add_student()
                elif act == '2':
                    put_rating()
                elif act == '0':
                    flag = 0
            else:
                save_db()  #сохранение данных в файл db_student.json
        # блок кода ученика
        case '2':
            flag = 1
            while flag == 1:
                last_name = input('введите фамилию ученика или 0 для выхода из программы\nВвод: ')
                if last_name == '0':
                    flag = 0
            else:
                see_rating(last_name)
