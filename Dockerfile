FROM python:3.9-slim
ENV DOCKER=true
ENV GIT_PYTHON_REFRESH=quiet
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y libcairo2 git build-essential && rm -rf /var/lib/apt/lists/*

RUN mkdir /data
COPY . /data/Hikka
WORKDIR /data/Hikka

RUN pip install --no-cache-dir -U -r requirements.txt

EXPOSE 8080

CMD ["python", "-m", "hikka"]
