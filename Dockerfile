FROM cepgbaseacr.azurecr.io/docker.io/openjdk:17-slim
WORKDIR /app
COPY . /app
RUN pip install Flask
CMD ["python", "src/app.py"]

