FROM python:3.12.10-slim

WORKDIR /mytestapp2

COPY app* req*.txt .env /mytestapp2/

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r reqs.txt

CMD ["python", "app1.py"]
