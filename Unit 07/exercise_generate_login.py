def login_name(first_name, middle_name, last_name, stu_id):
    
    if middle_name != '':
        save_login = first_name[:2]+last_name[:5]+middle_name[0]
    else:
        save_login = first_name[:2]+last_name[:5]
    save_login += stu_id[-3:]

    return save_login

print(login_name('Adam', 'Tim', 'Smith', '123456'))
