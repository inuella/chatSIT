from flask import Flask, render_template, request, jsonify
from gpt4 import question


app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    if request.method == 'POST':
        ask_box1_value = request.form['ask_box1']
        ask_box2_value = request.form['ask_box2']
        ask_box3_value = request.form['ask_box3']
        ask_box4_value = request.form['ask_box4']

        result1, result2, result3 = question(ask_box1_value, ask_box2_value, ask_box3_value, ask_box4_value)
        return jsonify({'result1': result1, 'result2': result2, 'result3': result3})
        #return render_template('result.html', result=result)


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)