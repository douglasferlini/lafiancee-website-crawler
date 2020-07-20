# VERSION 1
FROM python

WORKDIR /exec

ADD dress /exec

COPY run.sh /exec

RUN chmod +x /exec/run.sh

RUN mkdir /var/dresses/

RUN pip install scrapy

ENTRYPOINT [ "/exec/run.sh" ]