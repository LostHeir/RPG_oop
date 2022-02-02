import bcrypt
import sqlite3 as sql

salt = b'$2b$12$73UojrOL94QjzMGwdm1wp.'
# hashed = bcrypt.hashpw(passwd, salt)    Used to generate password

# user= 'user'
# con = sql.connect("users.db")
# cur = con.cursor()
# statement = "INSERT INTO users VALUES (?,?)"
# cur.execute(statement, (user,hashed))
# con.commit()
# statement = "SELECT username, password FROM users"
# cur.execute(statement)
# print(cur.fetchall())
#
# Used to inster data into db

def check_user(user, password):
    password = bcrypt.hashpw(password.encode('utf-8'), salt)
    con = sql.connect("users.db")
    cur = con.cursor()
    statement = f"SELECT username from users WHERE username=(?) AND Password = (?);"
    cur.execute(statement, (user,password))
    if not cur.fetchone():  # An empty result evaluates to False.
        return False
    else:
        return True

check_user('user', '1234')