FROM python:3.8.6-alpine
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
COPY . /home
ENV PYTHONPATH "${PYTHONPATH}:/home"

CMD python /home/app/main.py
