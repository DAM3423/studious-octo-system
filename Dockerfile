FROM python:3.7
MAINTAINER Dominic Marshall

RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO

WORKDIR  /WORK_REPO

ADD index.py .

CMD ["python", "-u", "index.py"]