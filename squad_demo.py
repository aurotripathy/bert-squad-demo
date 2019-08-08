
import sys
sys.path.append('../bert')

from run_eval_squad import SquadQA

from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

# TODO should these be globals
view_data = {'context' : 'nothing yet', 'question' : 'no question', 'answer' : 'no answer'}

@app.route('/squad_demo')
def upload_file():
   print("SQUAD is initializing:..wait!")
   # global squad_qa
   # squad_qa = SquadQA()
   # squad_qa.squad_setup_for_inference()
   print("--------------------------------")
   print("SQUAD initialized: Ready for Q&A")
   print("--------------------------------")
   return render_template('squad-form.html', result=view_data)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      print("Context:\n")
      print(request.form['context'])
      print("Question:\n")
      print(request.form['question'])
      view_data['context'] = request.form['context']
      view_data['question'] = request.form['question']
      view_data['answer'] = squad_qa.answer_question(request.form['context'],
                                                     request.form['question'])
      return render_template('squad-form.html', result=view_data)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug = True)
