FROM python:3.9.6

ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT="true"

WORKDIR /code
ADD requirements.txt /code
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
COPY . /code