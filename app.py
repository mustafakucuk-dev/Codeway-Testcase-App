import time
import os
from redis import Redis
from flask import Flask, redirect, url_for, render_template, request, session
import socket

app = Flask(__name__)

#redis_host = os.environ['REDIS_HOST']
#redis_port = os.environ['REDIS_PORT']
#cache = redis.Redis(host=redis_host, port=redis_port)

redis_host = "165.227.132.17"
redis_port = 6379
cache = Redis(host=redis_host, port=redis_port)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

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
    
