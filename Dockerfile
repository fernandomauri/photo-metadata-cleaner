FROM python:3.10-slim-buster

WORKDIR /app/

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "python3 metadata_cleaner.py & tail -f /dev/null"]
