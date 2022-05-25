def add_employee(my_list):
    data = r'C:\Education\Python\HomeWork\Phone_book\employees.txt'
    with open(data, 'a') as file:
        for i in my_list:
            file.write(f'{i} ')
        file.write('\n')

def save_employee(n, p):
    my_list = [n, p]
    return my_list