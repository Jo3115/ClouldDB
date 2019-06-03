import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='toor',
                             db='Users')


def add_user(values):
    cursor = connection.cursor()
    sql = '''insert into user(firstname,surname,username,password)
        VALUES('{0}','{1}','{2}','{3}');'''.format(values[0], values[1],
                                                   values[2],
                                                   values[3])
    cursor.execute(sql)
    connection.commit()


def remove_user(id):
    sql = '''DELETE FROM user WHERE userID='{0}';'''.format(id)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

if __name__ == '__main__':
    values = ['jame', 'smith', 'smith12', '1234']
    remove_user(5)
    cursor = connection.cursor()
    cursor.execute('SELECT * from user')
    print(cursor.fetchall())


"""
sql = '''CREATE TABLE user(
    userID int AUTO_INCREMENT,
    firstname text NOT NULL,
    surname text NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    PRIMARY KEY (userID))'''
"""


sql = '''insert into user(firstname,surname,username,password)
    VALUES('sam','smith','toor','root');'''


#cursor.execute(sql)

