from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

# TODO should these be globals
view_data = {'subject' : '', 'question' : '', 'answer' : ''}

@app.route('/upload')
def upload_file():
   return render_template('my-form.html', result=view_data['subject'])

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      print(request.form['subject'])
      view_data['subject'] = request.form['subject']
      return render_template('my-form.html', result=view_data['subject'])


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug = True)
