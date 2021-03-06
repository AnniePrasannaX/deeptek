from abc import ABC, abstractmethod
from minio import Minio
# from minio.error import S3Error
import MySQLdb as mdb
from flask import request
import sys
import mysql.connector
import glob

from config import *

client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=False
     )

class DataSourceBase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save(self,cursor,tablename):
        pass

    @abstractmethod
    def close(self,conn):
        pass



class MinioSource(DataSourceBase):
    
    
    def connect(self):
        # args=request.args
        # Make 'asiatrip' bucket if not exist.
        client = Minio(
            "10.197.0.53:32560",
            access_key="minio",
            secret_key="minio123",
            secure=False,
        )
        print("hello")
        found = client.bucket_exists("dbdemo")
        print("dfdhfhdfhdhk")
        if not found:
            client.make_bucket("dbdemo")
        dcmfiles = [dcmfile for dcmfile in glob.glob("dicomfile/*.dcm")]
        for dicomfile in dcmfiles:
            filename=dicomfile.split('/')[-1]
            result = client.fput_object("dbdemo", f"sample/88/"+filename, dicomfile)    
        print("welcome")    
        # client.fput_object(
        # "dbdemo", "demofiles", "../dicomfile/case2a_001.dcm",
        #  )  
          

    def save(self):
        # client.fput_object(
        # "dbdemo", "demofiles", "/dicomfile/case2a_001.dcm",
        # )
        # found = client.bucket_exists("dbdemo")
        # print("dfdhfhdfhdhk")
        # if not found:
        #     client.make_bucket("dbdemo")
        # dcmfiles = [dcmfile for dcmfile in glob.glob("dicomfile/*.dcm")]
        # for dicomfile in dcmfiles:
        #     filename=dicomfile.split('/')[-1]
        #     result = client.fput_object("dbdemo", f"sample/88/"+filename, dicomfile)    
        print("welcome")
        print("hii")  
    @staticmethod
    def close():
        print("hey")      

class MysqlSource(DataSourceBase):
    # @staticmethod
    def connect(self):
        print("hellooo")
        cnx = mysql.connector.connect(user='annie', password='annie123',
                              host='dwrapper2',
                              database='mysql')
        print("connected")
        # conn = mdb.connect(host=get_mysql_hostname(),user=get_mysql_username(), passwd=get_mysql_password(),
        #     db=get_mysql_dbname(),port=get_mysql_port())
        # cursor = conn.cursor()
        # return cursor,conn

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
        ob.save()
        ob.close()
    elif db == "Mysql":
        ob1 = MysqlSource()
        cursor,conn = ob1.connect()
        ob1.save(cursor, tablename)
        ob1.close(conn)

