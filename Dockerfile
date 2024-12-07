FROM python:3.11

RUN apt update
RUN mkdir /micron

WORKDIR /micron

COPY ./micron ./micron
COPY ./commands ./commands

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["bash"]
