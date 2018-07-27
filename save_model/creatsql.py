class CreatSql():
    def insert(self,table = None,data = None):
        table = "" if table is None else table
        data = {} if data is None else data
        keys = ",".join(data.keys())
        values = ",".join(["%s"]*len(data))
        sql = r'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table = table,keys=keys,values=values)
        return sql
    def updata(self,table = None,data = None):
        table = "" if table is None else table
        data = {} if data is None else data
        keys = ",".join(data.keys())
        values = ",".join(["%s"]*len(data))
        sql = "INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATA".format(table=table,keys=keys,values=values)
        updata = ",".join([" {key} = %s".format(key = key) for key in data])
        sql += updata
        return sql
    def delete(self,table = None,condition = None)
        table = "" if table is None else table
        condition = "" if data is None else data
        sql = "DELETE FROM {table} WHERE {condition}".format(table=table,condition=condition)
        return sql
    def select(self,table,condition):
        table = "" if table is None else table
        condition = "" if data is None else data
        sql = "SELECT * FROM {table} WHERE {condition}".format(table=table,condition=condition)
        return sql




sql = CreatSql()
data = {"name":"wbt"}
table = 'student1'
print(sql.updata(table=table,data=data))
