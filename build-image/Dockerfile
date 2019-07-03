FROM fusiondb/fusiondb:0.1.0-beta

MAINTAINER fusiondb version: 0.1.1-beta

WORKDIR /ws

COPY fusiondb/assembly /opt/fusiondb/assembly

ADD init.sh /opt/

EXPOSE 54322

CMD ["sh", "/opt/init.sh"]
