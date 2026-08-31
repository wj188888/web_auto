import pymysql


# 配置数据库信息,dict方式
db_conf = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'charset': 'utf8',
}

class DBConnect():

    def __init__(self, db_conf, database=""):
        self.db_conf = db_conf

        # 打开数据库
        self.db = pymysql.connect(db=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_conf)
        self.cursor = self.db.cursor()

    def select(self, sql):
        # sql是sql查询语句，用单引号进行关联
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 执行失败进行回滚
            self.db.rollback()

    def close(self):
        # 关闭游标和mysql数据库连接
        # self.cursor.close()
        self.db.close()

# 测试代码，select and delete  查询和删除
# if __name__ == '__main__':
#     db = DBConnect(db_conf, "product_db")
#     sql = 'select * from products'
#     results = db.select(sql)
#     print(results)
#
#     sql2 = 'delete from users where username="user2"'
#     results2 = db.execute(sql2)
#     print(results2)
