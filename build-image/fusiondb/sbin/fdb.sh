#!/usr/bin/env bash
export JAVA_HOME=/opt/jdk1.8.0_112
export SPARK_HOME=../thirdparty/spark-2.4.3-bin-hadoop2.7
export LIVY_HOME=../thirdparty/livy-0.5.0-incubating-bin

if [ $# != 1 ]; then
    echo "USAGE: fdb.sh start or stop"
    exit 1;
fi

if [ $1 = "start" ] ; then
    ./start-sql-server.sh --conf spark.sql.server.psql.enabled=true --conf spark.sql.server.binaryTransferMode=false --conf spark.sql.server.port=54322
fi

if [ $1 = "stop" ]; then
    ./stop-sql-server.sh
fi
