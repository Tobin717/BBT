from config import db
import mysql.connector
from utils import encrypt, checkPwd

conn = mysql.connector.connect(host=db['host'], user=db['user'], passwd=db['passwd'], 
                                database=db['database'], charset='utf8mb4')
db = conn.cursor()


def findUser(username):
    db.execute('select * from user_name where `user_name`=%s', (username,))
    result = db.fetchall()
    return result


def userLogin(username, password):
    db.execute('select * from user_name where `user_name`=%s', (username,))
    result = db.fetchone()
    # result若存在, 在本例中是一个list, [1, "abc", ".....加密密码....."]
    if result:
        if checkPwd(password, result[2]):
            return result
    # 密码错误或用户名不存在
    return None


def createUser(username, password):
    # 密码加密
    password = encrypt(password)
    db.execute('insert into user_name (`user_name`, `user_password`) values (%s, %s)', (username, password))
    # 对数据库进行修改(create, update, delete)的操作必须commit
    conn.connection.commit()
    return db.rowcount
