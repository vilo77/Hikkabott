FROM python:3.8-slim AS python-base
ENV DOCKER=true
ENV GIT_PYTHON_REFRESH=quiet
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1

RUN apt update && apt install libcairo2 git build-essential curl -y --no-install-recommends
RUN rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp/*

RUN mkdir /data

COPY . /data/Hikka
WORKDIR /data/Hikka

RUN pip install --no-warn-script-location --no-cache-dir -U -r requirements.txt
RUN curl -sL https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz | tar xzf - -C /usr/local/bin

EXPOSE 8080

CMD sh -c "ngrok http 8080 & python -m hikka"
