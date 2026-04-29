FROM python:3.11-slim
WORKDIR /app
RUN useradd -m -u 1000 appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app_fixed.py .
RUN mkdir -p files && chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "app_fixed.py"]
