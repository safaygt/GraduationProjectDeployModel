FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir flask flask-cors torch ultralytics pillow

COPY . .

RUN mkdir -p uploads processed_images

EXPOSE 5000

CMD ["python", "app.py"]
