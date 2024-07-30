import socket
from flask import Flask, request, make_response
import logging
import db_actions

app = Flask(__name__)


hostname = socket.gethostname()

logging.basicConfig(filename=f'/var/log/count_app/count_log_{hostname}.log', level=logging.INFO)


@app.route('/', methods=['GET'])
def counter():
    client_ip = request.headers.get('X-Real-IP')
    local_ip = db_actions.access(client_ip)

    db_actions.increment_count()

    res = make_response(f'internal: {local_ip}')

    if 'app_ip' not in request.cookies:
        res.set_cookie('app_ip', local_ip, max_age=300)

    return res


@app.route('/showcount', methods=['GET'])
def show_count():
    count = db_actions.get_count()
    return str(count)


app.run(host='0.0.0.0', port=8989)
