import string
import secrets
import random
import re

def check_password(password):
    password_pattern = "(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&/_=;:<>|#,\*\'\"\-\+\(\)\{\}\.\+\[\]])[A-Za-z\d@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]]{8,}$"
    return re.fullmatch(password_pattern, password) != None

pass_characters = string.ascii_lowercase + \
                        string.ascii_uppercase + \
                        string.digits + \
                        string.punctuation

password = ''.join(secrets.choice(pass_characters) for i in range(0, random.randint(6,16)))

if check_password(password):
    print(f'The password {password} complies with the policy')
else:
    print(f'The password {password} not complies with the policy')
