FROM --platform=linux/amd64 python:3.11-slim


WORKDIR /app

COPY ./SavedModel/dog_cnn.h5 ./SavedModel/dog_cnn.h5
COPY ./labels.csv ./labels.csv

COPY ./main.py ./main.py

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
