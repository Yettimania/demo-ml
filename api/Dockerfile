FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py justfile predict.py train.py ./

# Build model to store in container build.
RUN ["python","train.py"]

# Run Flask app on docker start
CMD ["python","app.py"]
