import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload_file():


    if request.method == 'POST':
        if 'file' not in request.files:
            print 'No file part'
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print 'No selected file'
            return redirect(request.url)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect('/')
    else:
        print 'elaw'
        return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')