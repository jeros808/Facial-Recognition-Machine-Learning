from __future__ import print_function
import sys
import os
from flask import Flask, render_template, Response, request, redirect, url_for
from camera import VideoCamera
buttons = 0
app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
  	  
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data', methods=['GET', 'POST'])
def data():
    return render_template('data.html')

@app.route('/data')
def button():
    print("go to data!")
    buttons = 1
    return render_template('data.html')
# @app.after_request
# def add_header(response):
#     response.cache_control.no_store = True
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '-1'
#     return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


