class DB:
    @staticmethod
    def connect():
        print('Connecting to the database')


class Proxy:
    __admin_password = 'admin'

    def set_password(self, password):
        Proxy.__admin_password = password

    def check_credentials(self):
        password = input('Enter the password: ')
        if password == Proxy.__admin_password:
            db = DB()
            db.connect()
        else:
            print('Wrong credentials')


def connect_to_db():
    proxy = Proxy()
    proxy.check_credentials()


if __name__ == '__main__':
    connect_to_db()
