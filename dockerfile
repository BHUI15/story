FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# expose the port that the container 
EXPOSE 8080

ENV FLASK_APP=main.py

CMD ["python", "main.py"]