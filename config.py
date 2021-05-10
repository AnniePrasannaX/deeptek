import sys
import json

with open("config.json","r")as fp:
	data = json.loads(fp.read())
	
def get_mysql_username():
	return data["Mysql"]["username"]
    
def get_mysql_password():
	return data["Mysql"]["password"]

def get_mysql_hostname():
	return data["Mysql"]["hostname"]

def get_mysql_dbname():
	return data["Mysql"]["dbname"]

def get_mysql_port():
	return data["Mysql"]["port"]	

def get_minio_username():
	return data["Minio"]["username"]

def get_minio_password():
	return data["Minio"]["password"]

def get_minio_hostname():
	return data["Minio"]["hostname"]

def get_minio_dbname():
	return data["Minio"]["dbname"]


	