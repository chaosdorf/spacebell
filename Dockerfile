FROM python:3.7
WORKDIR /app
CMD python spacebell.py
RUN apt-get update && apt-get -y install libpulse-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY spacebell.py .
