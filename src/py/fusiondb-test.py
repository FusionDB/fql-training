#!/usr/bin/env python
# coding: utf-8

# In[17]:


import psycopg2
import pandas as pd
connection = psycopg2.connect("host=localhost port=54322 dbname=default user=fdb sslmode=disable")
df = pd.read_sql(sql="SELECT * FROM VALUES (1, 1), (1, 2) AS t(a, b);", con=connection)
df.head()
df = pd.read_sql(sql="show databases;", con=connection)
df.head()


# In[18]:


df = pd.read_sql(sql="show tables;", con=connection)
df.head()


# In[9]:


## Load mysql table
df =pd.read_sql(sql="load 'mysql' options('url'='jdbc:mysql://localhost:53306/fdb_test','dbtable'='person','user'= 'root','password'='root') AS mysql_t2;", con=connection)
df =pd.read_sql(sql="SELECT * FROM mysql_t2;", con=connection)
df.head()


# In[10]:


## Load Postgres table
df =pd.read_sql(sql="load 'postgresql' options('url'='jdbc:postgresql://localhost:15430/fdb','dbtable'='person','user'= 'fdb','password'='fdb123') AS gp_t1;", con=connection)
df =pd.read_sql(sql="SELECT * FROM gp_t1;", con=connection)
df.head()


# In[21]:


## MySQL Table Join PostgreSQL Table
df =pd.read_sql(sql="CREATE table test as SELECT mysql_t2.* FROM mysql_t2 LEFT JOIN gp_t1 ON mysql_t2.id = gp_t1.id;", con=connection)
df =pd.read_sql(sql="SELECT * FROM test;", con=connection)
df.head()


# In[11]:


## Load oracle table 
df =pd.read_sql(sql="load oracle options('url'='jdbc:oracle:thin:SYSTEM/oracle@//localhost:49161/xe','dbtable'='FDBTEST20','user'= 'SYSTEM','password'='oracle') AS ora_t1;", con=connection)
df =pd.read_sql(sql="SELECT * FROM ora_t1 limit 10;", con=connection)
df.head()


# In[19]:


## Load HDFS parquet
df =pd.read_sql(sql="load 'hdfs://jdp-1:8020/tmp/spark-tpcds-data/web_site' format parquet AS web_site;", con=connection)
df =pd.read_sql(sql="SELECT * FROM web_site limit 10;", con=connection)
df.head()


# In[20]:


## Save table to hdfs
df =pd.read_sql(sql="save overwrite web_site TO 'hdfs://jdp-1:8020/tmp/web_site_test' FORMAT parquet;", con=connection)
df =pd.read_sql(sql="load 'hdfs://jpd-1:8020/tmp/web_site_test' format parquet AS mysql_t2_par;", con=connection)
df =pd.read_sql(sql="SELECT * FROM mysql_t2_par limit 10;", con=connection)
df.head()


# In[ ]:




