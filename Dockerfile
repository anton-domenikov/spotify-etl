FROM apache/airflow:2.1.0
COPY requirements.txt .
COPY .env .
RUN pip install -r requirements.txt