SQLSERVER_HOST = ""
SQLSERVER_PORT = ""
SQLSERVER_USER = ""
SQLSERVER_PASSWORD = ""
SQLSERVER_DB = ""
MYSQL_HOST = ""
MYSQL_PORT = ""
MYSQL_USER = ""
MYSQL_PASSWORD = ""
MYSQL_DB = ""
from creatsql import CreatSql
import pymysql
class SqlServerDB():
    def __init__(self):
        pass
class MysqlDB():
    def __init__(self):
        self.sql = CreatSql()
        try:
            self.db = pymysql.connect(host = MYSQL_HOST,user = MYSQL_USER,password = MYSQL_PASSWORD,port=MYSQL_PORT,db=MYSQL_DB)
            #self.cursor = self.db.cursor()#cursor相当于一个指针，在这里创建当存在多线程操作时，容易发生错误
        except Exception as e:
            print("数据库错误：",e.args)
    def insert(table,data):
        cursor = self.db.cursor()
        sql = self.sql.insert(table,data)
        try:
            if cursor.execute(sql,tuple(data.values())):
                print("插入数据成功")
                self.db.commit()
        except:
            print("插入失败")
            self.db.rollback()
    def updata(table,data):
        cursor = self.db.cursor()
        sql = self.sql.updata(table,data)
        try:
            if cursor.execute(sql,tuple(data.values())):
                print("更新数据成功")
                self.db.commit()
        except:
            print("更新失败")
    def __del__ (self):
        self.db.close()

