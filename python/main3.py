from createConnection import createConnection
from python.createUser import createUser
from updateUser import updateUser
from deleteUser import deleteUser
from readUsers import readUsers

def printMenu():
    print('1. Read all users')
    print('2. Create a new user')
    print('3. Update a user')
    print('4. Delete a user')
    print('5. Exit')

def main():
    while True:
        printMenu()
        action = input('Enter your action: ')
        conn = createConnection('./db/users.db')

        if action == '1':
            # read all users
            readUsers(conn)
        elif action == '2':
            # create a new user
            createUser(conn)
        elif action == '3':
            # update a user
            updateUser(conn)
        elif action == '4':
            # delete a user
            deleteUser(conn)
        elif action == '5':
            # exit the program
            print('Exiting program...')
            exit()
        else:
            # invalid action choice
            print('Invalid action choice. Please try again.')
            continue

main()
