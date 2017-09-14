FROM alpine:lastest

RUN apk update && apk add py2-pip && apk add git && \
    pip install git+https://github.com/MichaelMackus/mysql-transfer.git
