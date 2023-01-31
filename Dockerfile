FROM python:3.11.0-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get -y --no-install-recommends install \
     build-essential \
     libpq-dev \
     ca-certificates \
     python3-dev \
     gcc \
     python3-setuptools \
     postgresql-client \
     libssl-dev && \
     apt-get clean && \
     apt-get autoremove -y && \
     rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

RUN mkdir /src

WORKDIR /src

COPY . /src
