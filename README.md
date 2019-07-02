# FusionDB® FQL Training

**This repository provides a training for FusionDB FQL.**

In this training you will learn to:

* run SQL queries on FusionDB
* run SQL++ queries on FusionDB
* use FusionDB's SQL JDBC Server
* write the result of SQL queries to RDBMS (MySQL、PostgreSQL、Oracle)、S3、ADLS  and HDFS

### Requirements

* Remote HDFS or RDBMS (MySQL、PostgreSQL、Oracle)/S3/ADLS/GCP/OSS etc.
* Optional: Jupyter Notebook、PSequel

You **only need [Docker](https://hub.docker.com/r/fusiondb/fusiondb)** to run this training. </br>
You don't need Java, Scala, or an IDE.

For more information, please refer to [FusionDB Document](http://www.fusionlab.cn/zh-cn/fdb/quickstart.html)

### Quickstart

Fusiondb is a simple and powerful federated database engine.

## Quickstart

* Start FusionDB

```
docker run --name fdb -p 54322:54322 -itd fusiondb/fusiondb:0.1.0-beta
```

* Check FusionDB server

```
docker ps -a|grep fdb

lsof -i :54322
```

## Psycopg2 connecting FDB

```
import psycopg2
import pandas as pd
connection = psycopg2.connect("host=localhost port=54322 dbname=default user=fdb sslmode=disable")
df = pd.read_sql(sql="SELECT * FROM VALUES (1, 1), (1, 2) AS t(a, b);", con=connection)
df

df = pd.read_sql(sql="show databases;", con=connection)
df = pd.read_sql(sql="show tables;", con=connection)

df = pd.read_sql(sql="load 'hdfs://you_namenode_ip:8020/tmp/t1' format parquet as h1", con=connection)

df = pd.read_sql(sql="select * from h1", con=connection)
df.head()
```

For more information, please refer to [FusionDB Document](http://www.fusionlab.cn/zh-cn/fdb/quickstart.html)