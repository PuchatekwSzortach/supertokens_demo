FROM python:3.12.4-slim-bookworm

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . ./

CMD ["python", "app.py"]
