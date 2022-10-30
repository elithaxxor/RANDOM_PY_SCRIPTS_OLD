import json

'''
    * Simple Parsing Tool to Read/Write .json login files. 
'''

class Logins():
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

    def print_info(self):
        print(self.user)
        print(self.passw)

    def change_info(self):
        self.user = input('Input new User Name: ')
        self.passw = input('Input new Password: ')

    def save_json(self):
        login_info = {user: self.user, passw: self.passw}
        with open('login_details.json', 'w') as f:
            f.write(json.dumps(login_info, indent=3))

    def load_json(self, filename):
        with open(filename, 'r') as f:
            login_info = json.loads(f.read())
        self.user = login_info['user']
        self.passw = login_info['passw']


def main(): ## remove function to test each method
    user = Logins('test1', 'test2')
    user.print_info()
    user.change_info()
    user.print_info()

    user = Logins(None, None)
    user.print_info()
    user.change_info()
    user.print_info()

main()

