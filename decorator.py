from functools import wraps


class Information:
    @staticmethod
    def show_information():
        print('These are all of the required information')


class Login:
    def __init__(self):
        self.username = input('Enter username: ')
        self.password = input('Enter password: ')

    def check(self):
        if self.username == 'admin' and self.password == '123':
            return True
        return False


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        credentials = Login()
        if credentials.check():
            func()
        else:
            print('wrong credentials')

    return wrapper


@login_required
def access_info():
    information = Information()
    information.show_information()


if __name__ == '__main__':
    access_info()
