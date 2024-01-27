FROM python:3.9-slim
WORKDIR /app
COPY . .
#RUN pip install --no-cache-dir -r requirements.txt
#we don't need any requirements, because our code only uses standard libraries
CMD ["python", "main.py"]
