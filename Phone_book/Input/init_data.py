import pickle
employee_list = []

def load_employees():
    global employee_list
    with open(path, 'rb') as data:
        employee_list = pickle.load(data)
    return True

def read_data():
    global employee_list
    counter = 1
    print()
    for i in employee_list:
        print(f'{counter} - ', end='')
        for key, value in i.items():
            print(f'{key}: {value}', end=', ')
        print()
        counter +=1
    print(f'Общее количество сотрудников {len(employee_list)}')