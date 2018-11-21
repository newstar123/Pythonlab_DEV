# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：mysql.py
#   版本：0.1
#   作者：ctang
#   日期：2016-02-26
#   语言：Python 2.7.10
#   说明：对MySQLdb常用函数进行封装的类
#---------------------------------------

import MySQLdb
import time

class MySQL:
    error_code = ''     # MySQL错误号码
    _instance = None    # 本类的实例
    _conn = None        # 数据库conn
    _cur = None         # 游标

    _TIMEOUT = 30       # 默认超时时间30秒
    _timecount = 0

    def __init__(self, dbconfig):
        # 构造器：根据数据库连接参数，创建MySQL连接
        try:
            self._conn = MySQLdb.connect(host=dbconfig['host'],
                                         port=dbconfig['port'],
                                         user=dbconfig['user'],
                                         passwd=dbconfig['passwd'],
                                         db=dbconfig['db'],
                                         charset=dbconfig['charset'])
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            error_msg = 'MySQL error! ', e.args[0], e.args[1]
            print error_msg

            # 如果没有超过预设超时时间，则再次尝试连接
            if self._timecount < self._TIMEOUT:
                interval = 5
                self._timecount += interval
                time.sleep(interval)
                return self.__init__(dbconfig)
            else:
                raise Exception(error_msg)

        self._cur = self._conn.cursor()
        self._instance = MySQLdb

    def query(self, sql):
        # 执行SELECT语句
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "数据库错误代码：",e.args[0], e.args[1]
            result = False
        return result

    def update(self, sql):
        # 执行UPDATE及DELETE语句
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "数据库错误代码：",e.args[0], e.args[1]
            result = False
        return result

    def insert(self, sql):
        # 执行INSERT语句，如主键为自增长int，则返回新生成的ID
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql)
            self._conn.commit()
            #return self._conn.insert_id()
            #return True
            return "插入数据成功！"
        except MySQLdb.Error, e:
            #return False
            self.error_code = e.args[0]
            error_msg = e.args[1]
            return "插入数据失败，错误原因：" + error_msg

    def fetchAllRows(self):
        # 返回结果列表
        return self._cur.fetchall()

    def fetchOneRow(self):
        # 返回一行结果，然后游标指向下一行。到达最后一行以后，返回None
        return self._cur.fetchone()

    def getRowCount(self):
        # 获取结果行数
        return self._cur.rowcount

    def commit(self):
        # 数据库commit操作
        self._conn.commit()

    def rollback(self):
        # 数据库回滚操作
        self._conn.rollback()

    def __del__(self):
        # 释放资源（系统GC自动调用）
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        # 关闭数据库连接
        self.__del__()

if __name__ == '__main__':
    '''使用样例'''

    # 数据库连接参数
    dbconfig = {'host':'localhost',
                'port': 3306,
                'user':'root',
                'passwd':'abc123',
                'db':'lovehuihui',
                'charset':'utf8'}

    # 连接数据库，创建这个类的实例
    db = MySQL(dbconfig)

    # 操作数据库
    sql = "show tables"
    db.query(sql)
    result = db.fetchAllRows()
    print result

