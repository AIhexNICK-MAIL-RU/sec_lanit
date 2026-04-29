FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY config.yaml .
ENV FLASK_APP=app.py
ENV SECRET_KEY=hardcoded_secret_123
EXPOSE 5000
CMD ["python", "app.py"]
