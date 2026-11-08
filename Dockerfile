FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt  .
RUN pip install -r requirements.txt
COPY . .
CMD ["app", "app.py"]

docker build -t my-flask-app:1.0  .

docker run -d -p 5000:5000 --name my-container my-flask-app:1.0

curl http://localhost:5000
docker logs my-container
docker tag my-flask-app:1.0 username/my-flask-app:1.0
docker push username/my-flask-app:1.0
docker-compose up -d
