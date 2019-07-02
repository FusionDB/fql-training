Fusiondb is a simple and powerful federated database engine.

## First start FusionDB

* Start FusionDB in docker

```
docker run --name fdb -p 54322:54322 -itd fusiondb/fusiondb:0.1.0-beta

docker logs -f fdb

docker ps -a|grep fdb
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
connection = psycopg2.connect(“host=localhost port=5432 dbname=default user=xujiang sslmode=disable”)
df = pd.read_sql(sql=”SELECT * FROM VALUES (1, 1), (1, 2) AS t(a, b);”, con=connection)
df
a b
0 1 1
1 1 2
df = pd.read_sql(sql=”show databases;”, con=connection)
df = pd.read_sql(sql=”show tables;”, con=connection)

df = pd.read_sql(sql=”load ‘hdfs://jdp-1:8020/tmp/t1‘ format parquet as h1”, con=connection)

df = pd.read_sql(sql=”select * from h1”, con=connection)
df.head()
```

For more information, please refer to [FusionDB Document](http://www.fusionlab.cn/zh-cn/fdb/quickstart.html)
