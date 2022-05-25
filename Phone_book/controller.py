from Input import user_select, name, phone, remove
from Prog import add_employee, save_employee, show, delete
from Out import get_menu

def start():
    while True:
        get_menu()
        user_sel = user_select()
        if user_sel == 0:
            print('Пока!')
            break
        elif user_sel == 1:
            user_name = name()
            user_phone = phone()
            add_employee(save_employee(user_name, user_phone))
        elif user_sel == 2:
            show()
        elif user_sel == 3:
            rem = remove()
            delete(rem)