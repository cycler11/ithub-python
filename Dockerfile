FROM python:3.9-slim
WORKDIR /app
COPY search_module.py /app
CMD ["python", "search_module.py"]
