FROM tiangolo/uvicorn-gunicorn:python3.9-slim

LABEL maintainer="alamsyah"

ENV WORKERS_PER_CORE=4
ENV MAX_WORKERS=24
ENV LOG_LEVEL="warning"
ENV TIMEOUT="200"

RUN apt-get update
RUN apt-get install libgl1 gcc libglib2.0-0 -y
RUN rm -rf /var/lib/apt/lists # not necessary
RUN mkdir /yolov5-fastapi

COPY requirements.txt /yolov5-fastapi

COPY . /yolov5-fastapi

WORKDIR /yolov5-fastapi

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]