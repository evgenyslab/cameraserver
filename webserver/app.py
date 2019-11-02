from flask import Flask, Response
import requests
from flask import stream_with_context

app = Flask(__name__)

@app.route('/')
def hello_world():
    stream = requests.get('http://localhost:7777', stream=True)

    return Response(stream_with_context(stream.iter_content(chunk_size=8096)), content_type = stream.headers['content-type'])
    