FROM python:3.8.6-alpine@sha256:d5c924d85736fd74da89db7dfdb9169ae6032a1c838a4ece3969dbb03cdc1159
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
COPY . /home
ENV PYTHONPATH "${PYTHONPATH}:/home"

CMD python /home/app/main.py
