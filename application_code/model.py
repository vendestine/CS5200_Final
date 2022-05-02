import pymysql
from setting import DB_CONFIG
from tabulate import tabulate

class Mysql():
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)

    # create, update, and delete method
    def update(self, sql):
        print("process sql：{}".format(sql))
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
            return "back"
        finally:
            cursor.close()


    #read method
    def get_all(self,sql):
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()

# test
if __name__ == '__main__':
    print('')