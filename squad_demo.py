"""
User interface to drive the SQuAD demo
"""
import sys
sys.path.append('../bert')
import json
import random
from pudb import set_trace

from run_eval_squad import SquadQA

from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

def format_answer(answer):
   sample = json.loads(answer)

   out = ""
   set_trace()
   for s in sample[""]:
      out = out + 'Probability: ' + \
            '{0:.2f}'.format(s['probability']) + '   ' + \
            'Answer: ' +  s['text'] + '\n'

   return out

# TODO should these be globals
view_data = {'context' : 'nothing yet', 'question' : 'no question', 'answer' : 'no answer'}

@app.route('/squad_demo')
def upload_file():
   print("SQUAD is initializing:..wait!")
   global squad_qa
   squad_qa = SquadQA()
   squad_qa.squad_setup_for_inference()
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
      answer = squad_qa.answer_question(request.form['context'],
                                        request.form['question'])
      view_data['answer'] = format_answer(answer)
      return render_template('squad-form.html', result=view_data)

@app.route('/preset', methods = ['GET', 'POST'])
def preset():
   print("Preset was clicked.")
   if request.method == 'GET':
      contexts, questions = squad_qa.get_preset_qas()
      choice = random.randint(0, len(contexts) - 1) 
      print("Context:\n")
      print(contexts[0])
      print("Question:\n")
      print(questions[0])
      view_data['context'] = contexts[choice]
      view_data['question'] = questions[choice]
      view_data['answer'] = ""
   
   return render_template('squad-form.html', result=view_data)

@app.route('/clear', methods = ['GET', 'POST'])
def clear():
   print("Clear was clicked.")
   if request.method == 'GET':
      view_data['answer'] = ""
   
   return render_template('squad-form.html', result=view_data)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug = True)
