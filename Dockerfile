FROM python:3.8-slim-buster

ADD web_app ./newsletter/web_app/

ADD database.db ./newsletter

ADD requirements.txt ./newsletter

ADD main.py ./newsletter

ADD build.sh ./newsletter

RUN sh ./newsletter/build.sh

CMD python3 ./newsletter/main.py