import sqlite3

# Connect to the users.db file
conn = sqlite3.connect('./db/users.db')

#Create a cursor object 
cursor = conn.cursor()

def thanks():
    print("Ait felagi")

print ('Do you want to print out the users? (y/n)')
choice = input()

if choice.lower() == 'y':
    #Execute the Select statement 
    cursor.execute('SELECT Id, firstName, lastName, email, phone FROM users;')

    rows = cursor.fetchall()
    for row in rows:
        print(
            f"ID: {row[0]}, FullName: {row[1]}{row[2]}, "
            f"Email: {row[3]}, "
            f"Phone: {row[4]}"
        ) 

cursor.close()
conn.close()

if choice.lower() == 'n':
    thanks()


