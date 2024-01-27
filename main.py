from bf import read_passwords
import random
import string

class SystemStub:
    login: str
    password: str

    def __init__(self, login: str = 'admin'):
        self.login = login
        self.password = ''

    def auth(self, password: str):
        is_password_blank = self.password == ''
        if is_password_blank:
            random_value = random.randrange(1, 10)
            is_winning_condition = random_value == 7
            if is_winning_condition:
                self.password = password
                return "success"
            else:
                return "PASSWORD IS INVALID"

        else:
            is_same_password = password == self.password
            if is_same_password:
                return "success"
            else:
                return "invalid"

def do_bruteforce(system_stub, filename):
    passwords = read_passwords(filename)  #bf module fuction!!
    for password in passwords:
        if system_stub.auth(password) == '!!! SUCCESS !!!':
            return password
    return None

if __name__ == "__main__":
    s = SystemStub()
    found_password = do_bruteforce(s, 'passwords.txt')
    if found_password:
        print(f"Password found: {found_password}")
    else:
        print("Password not found.")

