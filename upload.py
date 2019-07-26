from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   # return render_template('upload.html')
   return render_template('my-form.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      # f = request.files['file']
      print(request.form['message'])
      
      # f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug = True)
