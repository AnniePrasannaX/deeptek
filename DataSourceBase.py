from abc import ABC, abstractmethod
from minio import Minio
# from minio.error import S3Error
import MySQLdb as mdb
import sys

from config import *

class DataSourceBase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save(self,cursor, tablename):
        pass

    @abstractmethod
    def close(self,conn):
        pass

class MinioSource(DataSourceBase):

    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
     )

    def connect(self):
        # Make 'asiatrip' bucket if not exist.
        # client = Minio(
        # "play.min.io",
        # access_key="Q3AM3UQ867SPQQA43P2F",
        # secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        # )
        found = client.bucket_exists("dbdemo")
        if not found:
            client.make_bucket("dbdemo")
        client.fput_object(
        "dbdemo", "demofiles", "/dicomfile/case2a_001.dcm",
         )  
        print("hello")  

    def save(self,cursor, tablename):
        # client.fput_object(
        # "dbdemo", "demofiles", "/dicomfile/case2a_001.dcm",
        # )
        print("hii")  

    def close(self,conn):
        print("hey")      

class MysqlSource(DataSourceBase):
    def connect(self):
        print("connected")
        conn = mdb.connect(get_mysql_hostname(), get_mysql_username(), get_mysql_password(), get_mysql_dbname(),get_mysql_port())
        cursor = conn.cursor()
        return cursor,conn

    def save(self,cursor, tablename):
        sql = "INSERT INTO sample (name, place) VALUES (%s, %s)"
        val = ("John", "USA")
        # query = "SELECT * FROM {}".format(tablename)
        cursor.execute(query)
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)
        mdb.commit()
        print("saved")

    def close(self,conn):
        conn.close()
        print("closed")               

if __name__ == "__main__":

    db = sys.argv[1]
    tablename = sys.argv[2]
    
    if db == "Minio":
        ob = MinioSource()
        ob.connect()
        ob.save(cursor,tablename)
        ob.close(conn)
    elif db == "Mysql":
        ob1 = MysqlSource()
        cursor,conn = ob1.connect()
        ob1.save(cursor, tablename)
        ob1.close(conn)



