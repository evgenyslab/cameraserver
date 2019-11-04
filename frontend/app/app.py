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

settings = {'example1': 'value', 'example2': 'value2'}

@app.route('/settings')
def list_settings():
    return Response(settings)

@app.route('/settings/<path:setting>')
def get_setting(setting):
    return Response(settings.get(setting))

@app.route('/settings/<path:setting>/<path:value>',  methods=['GET', 'PUT', 'POST'])
def set_setting(setting, value):
    settings[setting] = value
    return f"You set {setting} and {value}"

@app.route('/settings/<path:setting>', methods=['DELETE'])
def delete_setting(setting):
    return Response(settings.pop(setting, None))


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)