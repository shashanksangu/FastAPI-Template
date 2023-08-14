FROM python:3.9

LABEL maintainer="Shashank Sangu <sangushashanksai@gmail.com>"

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 8000:8000

RUN apt-get update -y

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

# CMD ["uvicorn", "main:app", "--host 0.0.0.0", "--workers 8"]

CMD ["gunicorn", "main:app", "--workers 4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]

# CMD [ "uvicorn", "main:app", "--host 0.0.0.0", "--reload" ]