FROM python:3.7-slim
RUN pip install flask 
RUN pip install redis

ARG REDIS_HOST = "165.227.132.17"
ARG REDIS_PORT = 6379
ARG REDIS_PASS

ENV DB_HOST = $REDIS_HOST
ENV DB_PORT = $REDIS_PORT
ENV DB_PASS = $REDIS_PASS


WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT ["python"]
CMD ["/app/app.py"]