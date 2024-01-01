import mysql.connector

Info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="demo"
)
if Info.is_connected():
    print("Successfully connect")

cursor = Info.cursor()
def register(data):
    try:
        cursor.execute('INSERT INTO `users` (`email`, `username`, `password`) VALUES (%s, %s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print('Exception is ', e)
        return False

def onclick(data):
    try:
        cursor.execute('SELECT * FROM `user` WHERE `username` = %s AND `password` = %s', data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False


def getAllUsers():
    try:
        cursor.execute('SELECT * FROM `users`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False