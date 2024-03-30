FROM nikolaik/python-nodejs:python3.8-nodejs14-slim

RUN apt-get -y update && apt-get -y install cron

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1
WORKDIR /trippyfinal/Backend
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000

WORKDIR /trippyfinal/Frontend
COPY Frontend/package.json ./
RUN npm install
RUN npm audit fix --force
EXPOSE 3000


WORKDIR /trippy

COPY . .
COPY runner.sh /scripts/runner.sh
RUN chmod +x /scripts/runner.sh

ENTRYPOINT ["/bin/sh","/scripts/runner.sh"]
