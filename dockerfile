FROM python:3

WORKDIR /app

COPY DataSourceBase.py .

COPY config.py .

COPY config.json .

RUN pip3 install flask requests mysqlclient Minio mysql-connector-python

EXPOSE 8000

#RUN mkdir -p /tmp/pyth

#COPY files/anju/* /tmp/pyth/

CMD ["python", "/app/DataSourceBase.py","Mysql","sample"]