import bcrypt 
from createConnection import createConnection
from python.createUser import createUser

def main():

    conn = createConnection('./db/users.db')
    with conn:

        firstName = input('Enter your first name: ')
        lastName = input('Enter your last name: ')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        phone = input('Enter your phone number: ')



    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    user = (firstName, lastName, email, hash.decode(),phone)

    createUser(conn, user)

main()
