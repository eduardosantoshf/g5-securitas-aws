FROM python:3.10-slim

WORKDIR /usr/app
COPY ./requirements.txt .
ENV PYTHONPATH "${PYTHONPATH}:/usr/app"

RUN apt-get update
RUN apt-get install -y libmariadb3 libmariadb-dev
RUN apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
