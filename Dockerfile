FROM python:3.8-slim AS python-base
ENV DOCKER=true
ENV GIT_PYTHON_REFRESH=quiet
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1

RUN apt update && apt install libcairo2 git build-essential -y --no-install-recommends
RUN rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp/*

RUN mkdir /data

COPY . /data/Hikka
WORKDIR /data/Hikka

RUN pip install --no-warn-script-location --no-cache-dir -U -r requirements.txt

EXPOSE 8080

CMD ["python", "-m", "hikka"]
