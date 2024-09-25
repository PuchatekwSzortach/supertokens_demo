FROM python:3.12.4-slim-bookworm

WORKDIR /app

# Setup PYTHONPATH
ENV PYTHONPATH=.

# Setup bashrc
COPY .bashrc /root/.bashrc

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . ./

CMD ["python", "run_app.py"]
