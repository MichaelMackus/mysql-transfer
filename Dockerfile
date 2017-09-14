FROM alpine:lastest

RUN apk update && apk add py2-pip && apk add git && \
    apk add mariadb-client                       && \
    apk add py-mysqldb                           && \
    pip install pyaml                            && \
    pip install git+https://github.com/MichaelMackus/mysql-transfer.git

