import locale
import secrets
import string
import random

pass_characters = string.ascii_lowercase + \
                        string.ascii_uppercase + \
                        string.digits + \
                        string.punctuation


while True:
    try:
        amount=int(input('Type the password amount to generate: '))
    except ValueError:
        print('The value typed is invalid. must type a integer number')
    else:
        break

print(f'Generating {locale.format_string("%2d", amount, grouping=True)} passwords')
for i in range(1, amount):
    password = ''.join(secrets.choice(pass_characters) for i in range(0, random.randint(6,16)))
    try:
        with open('random_passwords.txt','a') as pass_file:
            pass_file.write(password+'\n')
    except PermissionError as error:
        print('Faild when attempt access to the random_password.txt, verify that is closed')
        print(f'Error: {error}')
        exit()
