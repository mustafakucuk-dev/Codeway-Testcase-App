FROM python:3.7-slim
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask 
RUN pip install redis
WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT ["python"]
CMD ["/app/app.py"]