import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            Username varchar(255),
            Language varchar(3),
            Time int NOT NULL,
            Day int NOT NULL,
            Week int NOT NUll,
            Forever int NOT NULL,
            Read VARCHAR (8000),
            Friends int NOT NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    def update_language(self, language, id):
        sql = f"""UPDATE Users SET Language = ?  WHERE id = ?"""
        return self.execute(sql, parameters=(language, id), commit=True)

    def select_user(self, id):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE id = ?"
        return self.execute(sql, parameters=(id,), fetchone=True)

    def select_all_users(self):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)


    def add_user(self, id: int, name: str, username: str, language: str, time: int,  day: int = 0, week: int = 0, forever: int = 0, read: str = "0", friends: int = 0 ):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, Username, Language, Time, Day, Week, Forever, Read, Friends) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, username, language, time, day, week, forever, read,  friends), commit=True)


    def search_user(self, name):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"""SELECT * FROM Users WHERE Name LIKE "%{name}%" LIMIT 50;"""
        return self.execute(sql, fetchall=True)

    def search_user_random(self):
        sql = f"""SELECT * FROM Users ORDER BY RANDOM() LIMIT 50;"""
        return self.execute(sql, fetchall=True)


#####################################################################################################################################################################################

    def friends_return(self, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        SELECT  Friends  FROM Users WHERE id = ? 
          """
        return self.execute(sql, parameters=(id,), fetchone=True)

#####################################################################################################################################################################################

    def friends_update(self, friends, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
          UPDATE Users SET Friends = ? WHERE id=?
          """
        return self.execute(sql, parameters=(friends, id), commit=True)

######################################################################################################################################################################################

    def time_update(self, new_time, id):
        sql = f"""
              UPDATE Users SET Time = ? WHERE id=?
               """
        return self.execute(sql, parameters=(new_time, id), commit=True)

    def return_four(self, id):
        sql = f"""
        SELECT Day, Week, Forever, Read FROM Users  WHERE id = ? 
          """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def update_four(self, day,week, forever, read, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
           UPDATE Users SET Day = ?, Week =?, Forever = ?, Read = ? WHERE id=?
           """
        return self.execute(sql, parameters=(day,week, forever, read, id), commit=True)


    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)




    def delete_block_user(self, id):
        self.execute(f"DELETE FROM Users WHERE id = {id}", commit=True)





#########################################################################################################################################################################################
    def create_table_hadislar(self):
        sql = """
        CREATE TABLE Hadislar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            UZBEKCHA varchar(4096) NOT NULL,
            UZBEKCHA_SARLAVHA varchar(4096) NOT NULL,
            RUSCHA varchar(4096) NOT NULL,
            RUSCHA_SARLAVHA varchar(4096) NOT NULL
            );
"""
        self.execute(sql, commit=True)


    def search_hadis_uz(self, name):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"""SELECT * FROM Hadislar WHERE UZBEKCHA_SARLAVHA LIKE "%{name}%" LIMIT 50;"""
        return self.execute(sql, fetchall=True)


    def search_hadis_ru(self, name):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"""SELECT * FROM Hadislar WHERE RUSCHA_SARLAVHA LIKE "%{name}%" LIMIT 50;"""
        return self.execute(sql, fetchall=True)

    def search_hadis_random_uz(self):
        sql = f"""SELECT * FROM Hadislar  ORDER BY RANDOM() LIMIT 50;"""
        return self.execute(sql, fetchall=True)


    def search_hadis_random_ru(self):
        sql = f"""SELECT * FROM Hadislar   ORDER BY RANDOM() LIMIT 50;"""
        return self.execute(sql, fetchall=True)


    def select_all_hadis(self):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Hadislar"
        return self.execute(sql, fetchall=True)

    def add_hadis_3(self, UZ,UZ_S, RU, RU_S):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
              INSERT INTO Hadislar(UZBEKCHA, UZBEKCHA_SARLAVHA, RUSCHA, RUSCHA_SARLAVHA ) VALUES(?, ?, ?, ?)
              """
        self.execute(sql, parameters=(UZ, UZ_S,  RU, RU_S), commit=True)

    def random_hadis(self):
        return self.execute("""SELECT * FROM Hadislar ORDER BY RANDOM() LIMIT 1;""", fetchone=True)


    def count_hadis(self):
        return self.execute("SELECT COUNT(*) FROM Hadislar;", fetchone=True)

    def top_day(self):
        return self.execute("""
            SELECT *
            FROM Users
            ORDER BY Day DESC LIMIT 10
        """, fetchall=True)

    def top_week(self):
        return self.execute("""
            SELECT *
            FROM Users
            ORDER BY Week DESC LIMIT 10
        """, fetchall=True)

    def top_forever(self):
        return self.execute("""
            SELECT *
            FROM Users
            ORDER BY Forever DESC LIMIT 10
        """, fetchall=True)

    def update_day(self):
        return self.execute("""UPDATE Users SET Day = 0;""", commit=True)

    def update_week(self):
        return self.execute("""UPDATE Users SET Week = 0;""", commit=True)

    def create_table_book(self):
        sql = """
        CREATE TABLE Kitoblar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            BookName VARCHAR(1000),
            BookId VARCHAR(1000)
 
            )
"""
        self.execute(sql, commit=True)

    def book_save(self, book_name, book_id):
        sql = """
              INSERT INTO Kitoblar(BookName, BookId) VALUES(?, ?)
              """
        self.execute(sql, parameters=(book_name, book_id), commit=True)

    def book_return(self):
        sql = f"""
           SELECT * FROM Kitoblar;
             """
        return self.execute(sql, fetchall=True)

    def book_return_1(self, id):
        return self.execute( f"""SELECT BookId FROM Kitoblar WHERE id = {id} """,fetchone=True)

    def create_table_week(self):
        sql = """
        CREATE TABLE Hafta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Week int 
        )
        """
        self.execute(sql, commit=True)

    def return_day(self):
        sql = f"""
        SELECT  Week  FROM Hafta
          """
        return self.execute(sql, fetchone=True)

    def return_day_insert(self, update):
        sql = """
              INSERT INTO Hafta(Week) VALUES(?)
              """
        return self.execute(sql,parameters=(update,), commit=True)


    def updata_day_w(self, update):
        sql = f"""UPDATE Hafta SET Week = ? """
        return self.execute(sql, parameters=(update,), commit=True)



    def drop(self):
        return self.execute("DROP TABLE Users", commit=True)






def logger(statement):
    pass


