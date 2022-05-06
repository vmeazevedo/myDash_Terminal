FROM python:3.8

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "myDash_Terminal.py"]
