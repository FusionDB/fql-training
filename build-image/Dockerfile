FROM centos

MAINTAINER fusiondb version: 0.1.0-beta

RUN yum install tmux -y

WORKDIR /ws

COPY jdk1.8.0_112 /opt/jdk1.8.0_112

COPY fusiondb /opt/fusiondb

ADD init.sh /opt/

EXPOSE 54322

CMD ["sh", "/opt/init.sh"]
