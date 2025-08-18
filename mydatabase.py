from sqlite3 import connect
import bcrypt


class Database:
    db = None

    @staticmethod
    def connect_database():
        Database.db = connect('number.db')
        cursor = Database.db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, email text UNIQUE NOT NULL, password BLOB NOT NULL)')
        cursor.execute('CREATE TABLE IF NOT EXISTS fact_table(id integer PRIMARY KEY, email text NOT NULL, fact text NOT NULL)')

        Database.db.commit()
        print('Connected Successfully')

    @staticmethod
    def hash_password(password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    @staticmethod
    def insert_data(email, password):
        password = Database.hash_password(password)

        sql = 'INSERT INTO users (email, password) VALUES(?, ?)'
        val = (email, password)
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()

    @staticmethod
    def is_valid(email):
        sql = f"SELECT * FROM users WHERE email='{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            return False
        else:
            return True

    @staticmethod
    def is_exist(email, password):

        sql = f"SELECT * FROM users WHERE email = '{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:

            try:
                if password and bcrypt.checkpw(password.encode('utf-8'), result[0][2]):
                    return True
                else:
                    return False
            except Exception as e:
                print(e)

        return False

    @staticmethod
    def insert_fact(email, fact):
        sql='INSERT INTO fact_table (email, fact) VALUES (?, ?)'
        val = (f'{email}', f'{fact}')
        cursor = Database.db.cursor()
        cursor.execute(sql, val)
        Database.db.commit()


    @staticmethod
    def get_facts(email):
        sql = f"SELECT * FROM fact_table WHERE email = '{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result