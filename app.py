import os
from flask import Flask, request, redirect, url_for

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'par2', 'zip', 'xls'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/list", methods=['GET'])
def list():
    return """
    <!doctype html>
    <title>Get Files</title>
    <h1>Get Files</h1>
    <p>%s</p>
    """ % "<br>".join([str(x) for x in os.listdir(app.config['UPLOAD_FOLDER'])])

@app.route("/upload", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        print(request.files['file'])
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('index'))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="/upload" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join([str(x) for x in os.listdir(app.config['UPLOAD_FOLDER'])])
