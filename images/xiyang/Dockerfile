FROM python:3

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -U Flask
RUN pip install --no-cache-dir requests

VOLUME [ "/code" ]
ADD . /code
WORKDIR /code

EXPOSE 8080
CMD ["python3", "server.py"]