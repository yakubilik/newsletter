FROM python:3.8-slim-buster

ADD web_app ./newsletter/web_app/

ADD requirements.txt ./newsletter

ADD build.sh ./newsletter

RUN sh ./newsletter/build.sh

ADD add_admin.py ./newsletter

RUN python ./newsletter/add_admin.py

ADD main.py ./newsletter

CMD ["python3","./newsletter/main.py"]