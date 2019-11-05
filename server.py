from flask import Flask, Response, request
import requests, os
from collections import defaultdict
from flask import stream_with_context, send_from_directory

app = Flask(__name__, static_folder="webapp/build")

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def serve(u_path):
    # print("Hello")
    if u_path != "" and os.path.exists(app.static_folder + '/' + u_path):
        return send_from_directory(app.static_folder, u_path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


# settings = defaultdict(lambda: "default")
#
# @app.route('/settings')
# def list_settings():
#     return Response(settings)
#
# @app.route('/settings/<path:setting>')
# def get_setting(setting):
#     return Response(settings[setting])
#
# @app.route('/settings/<path:setting>/<path:value>',  methods=['GET', 'PUT', 'POST'])
# def set_setting(setting, value):
#     settings[setting] = value
#     return f"You set {setting} and {value}"
#
# @app.route('/settings/<path:setting>', methods=['DELETE'])
# def delete_setting(setting):
#     return Response(settings.pop(setting, None))


if __name__ == '__main__':
    app.run(host='0.0.0.0',use_reloader=True, port=5000, threaded=True)