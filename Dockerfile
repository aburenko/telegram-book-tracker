FROM python:3.8-slim AS bot

ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv

RUN mkdir -p /bot
ADD . /bot

WORKDIR /bot
RUN pip3 install -r requirements.txt
RUN chmod +x ./source/bot.py

CMD python3 ./source/bot.py
