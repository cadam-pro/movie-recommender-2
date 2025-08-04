FROM python:3.10-slim

WORKDIR /project

RUN apt-get update && apt-get install -y make

COPY requirements.in .
RUN pip install --no-cache-dir -r requirements.in

COPY . .

CMD ["tail", "-f", "/dev/null"]
