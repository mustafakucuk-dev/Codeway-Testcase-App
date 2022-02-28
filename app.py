import time
import os
from redis import Redis
from flask import Flask, redirect, url_for, render_template, request, session
import socket

app = Flask('flask-cloudbuild')

redis_host = os.environ['DB_HOST']
redis_port = os.environ['DB_PORT']
redis_pass = os.environ['DB_PASSWORD']

cache = Redis(host=redis_host, port=redis_port, password=redis_pass)

def get_hit_count():
    try:
        return cache.incr('hits')
    except Redis.exceptions.ConnectionError as exc:
        raise exc


@app.route('/')
def hello():
    count = get_hit_count()
    return 'I have been visited {} times ! \n'.format(count)

@app.route('/changeDatabase', methods=['POST'])
def changeDB():
    global redis_host, redis_port, cache
    print(redis_host)
    print(redis_port)
    request_data = request.get_json()
    redis_host = request_data["REDIS_HOST"]
    redis_port = request_data["REDIS_PORT"]
    test_db = socket.socket()
    try:
        test_db.connect((redis_host, int(redis_port)))
        cache = Redis(host=redis_host, port=redis_port)
        return "DB Endpoint Changed To : " + str(redis_host)+ " : " + str(redis_port)
    except Exception as e:
        return "Something's wrong with given endpoint -> " + str(redis_host) + " : " + str(redis_port) + "\n Exception is " + str(e)
    finally:
        test_db.close()
    
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)