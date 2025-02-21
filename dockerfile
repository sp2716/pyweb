FROM python:3-slim
EXPOSE 5000
EXPOSE 44818
WORKDIR /usr/src/app

RUN apt-get update
RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install nano
RUN apt-get install curl -y

COPY . .
RUN useradd app
USER app
CMD ["python","main.py"]