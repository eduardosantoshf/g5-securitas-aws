FROM python:3.10

WORKDIR /usr/app/src
COPY ./requirements.txt /usr/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /usr/app/requirements.txt

COPY ./src /usr/app/src

EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:/usr/app/src"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
