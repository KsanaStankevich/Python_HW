def delete(delll):
    # f = open("C:\Education\Python\HomeWork\Phone_book\employees.txt","r")
    # lines = f.readlines()
    # f.close()

    # f = open("C:\Education\Python\HomeWork\Phone_book\employees.txt","w")
    # for line in lines:
    #     if line != delll:
    #         f.write(line)
    # f.close()
    with open("C:\Education\Python\HomeWork\Phone_book\employees.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if delll not in line:
                f.write(line)
        f.truncate()