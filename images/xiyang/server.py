from flask import Flask, make_response, jsonify
from multiprocessing import Pool, cpu_count
import socket
import time

app = Flask(__name__)

@app.route('/')
def page():
    return make_response(jsonify({
        "/": "root info page:v1.01",
        "/ping": "test ping",
        "/loadtest/cpu": "test cpu intensive task",
        "/loadtest/memory": "test memory intensive task"
    }), 200)

@app.route('/ping')
def ping():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return "ping received on " + hostname + " " + hostip + "\n"

@app.route('/loadtest/memory/<int:size>/<int:seconds>')
def memory(size, seconds):
    try:
        dummy = 'A' * 1024 * 1024 * size
    except MemoryError:
        return make_response("Ran out of memory", 400)
    
    t_end = time.time() + seconds
    while time.time() < t_end:
        continue
    dummy = ''

    return make_response("Memory test finish", 200)

def f(x):
    loop_count = 1024 * 1024 * 128
    while loop_count > 0:
        x * x
        loop_count -= 1

@app.route('/loadtest/cpu/<int:cpus>')
def cpu(cpus):
    print('Number of cpus available: %d' % cpu_count())
    if (cpus > cpu_count()):
        return make_response("Requested cpus > number of cores available.", 400)

    print('-' * 20)
    print('Running load on CPU(s)')
    print('Utilizing %d cores' % cpus)
    print('-' * 20)
    pool = Pool(cpus)
    pool.map(f, range(cpus))
    pool.close()

    return make_response("CPU test finish", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)