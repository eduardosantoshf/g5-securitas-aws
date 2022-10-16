FROM python:3.9
COPY . /code/
WORKDIR /code/
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD ["python3","-u", "main.py"]