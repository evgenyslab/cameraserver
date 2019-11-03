from flask import Flask, Response, request
import requests, os
from flask import stream_with_context, send_from_directory

app = Flask(__name__, static_folder="build")

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def serve(u_path):
    print("Hello")
    if u_path != "" and os.path.exists(app.static_folder + '/' + u_path):
        return send_from_directory(app.static_folder, u_path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/stream')
def hello_world():
    stream = requests.get('http://localhost:7777', stream=True)

    return Response(stream_with_context(stream.iter_content(chunk_size=8096)), content_type = stream.headers['content-type'])
    
@app.route('/settings/<path:setting>/<path:value>')
def settings(setting, value):

    return f"You set {setting} and {value}"