from flask import Flask, url_for, render_template, jsonify
from flask import request, redirect, session, abort
from flask_sqlalchemy import SQLAlchemy
from gpt4 import question

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\test\\test.db'
db = SQLAlchemy(app)

def allow_specific_ip_pattern(func):
    def wrapper(*args, **kwargs):
        remote_ip = request.remote_addr

        # '192'로 시작하는 아이피만을 허용
        if not remote_ip.startswith('172'):
            return "서구청 내부망에서 이용해주세요."

        return func(*args, **kwargs)

    return wrapper

@app.errorhandler(404)
def page_not_found(error):
     return render_template('page_not_found.html'), 404

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))
	count = db.Column(db.String(80))

	def __init__(self, username, password, count):
		self.username = username
		self.password = password
		self.count = count





@app.route('/', methods=['GET', 'POST'])

def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = request.form['username']
			return render_template('1index.html')
		return render_template('bodo.html')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return 'Dont Login'
		except:
			return "Dont Login"
		
'''
@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'], 
			email=request.form['email'])

		db.session.add(new_user)
		db.session.commit()
		return render_template('login.html')
	return render_template('register.html')
'''

@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		app.secret_key = "123123123"
		app.run(host='0.0.0.0', debug=True)