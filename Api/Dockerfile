FROM python:3.12.0

WORKDIR /app

COPY ./SavedModel/dog_cnn.h5 ./SavedModel/dog_cnn.h5
COPY ./labels.csv ./labels.csv

COPY ./main.py ./main.py

RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
