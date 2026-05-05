FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential
RUN pip install fastapi uvicorn
COPY . .
EXPOSE 8000

CMD ["uvicorn", "application_controller:app", "--port", "8000"]