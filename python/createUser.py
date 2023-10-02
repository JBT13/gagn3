def createUser(conn, user):

    sql = '''INSERT INTO users(firstName, lastName, email, password, phone) VALUES (?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql ,user )
    conn.commit()
    return True