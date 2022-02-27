FROM python:3.7-slim
RUN pip install virtualenv
RUN virtualenv env
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
RUN pip install flask 
RUN pip install redis
WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT ["python"]
CMD ["/app/app.py"]