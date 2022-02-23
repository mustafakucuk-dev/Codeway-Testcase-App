FROM python:3.7-slim
RUN pip install flask
WORKDIR /app
COPY app.py /app/app.py
ARG DB_HOST="localhost"
ARG DB_PORT=6379
ENV REDIS_HOST=${DB_HOST}
ENV REDIS_PORT=${DB_PORT}
ENTRYPOINT ["python"]
CMD ["/app/app.py"]