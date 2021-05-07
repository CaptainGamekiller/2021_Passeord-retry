
password = 'a123456'
i = 3
while True:
    pwd = input('Please type the password: ')
    if pwd == password:
        print('Login successfully!')
        break
    else:
        i -= 1
        print('Wrong password! You still have ', i , ' chance(s).')
        if i == 0:
            print('You can try after 10 minutes!')
            break
