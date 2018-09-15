from flask import Flask, render_template, request
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('index.html',
		name='Nik')

@app.route('/tasks')
def get_tasks():
	tasks = ['Task 1', 'Task 2',
			'Task 3']
	now = datetime.now()
	show_time = False
	return render_template('tasks.html',
		tasks=tasks,
		now=now,
		show_time=show_time)


@app.route('/bio')
def get_bio():
	name = request.args.get('name')
	age = request.args.get('age')
	return "Your name is {} and age is {}".format(name, age)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'GET':
		return render_template('upload.html')
	elif request.method == 'POST':
		name = request.form.get('name')
		age = request.form.get('age')
		cgpa = request.form.get('cgpa')
		with open('student.csv', 'a') as f:
			writer = csv.writer(f)
			writer.writerow([name, age, cgpa])

		photo = request.files.get('photo')
		photo.save("photos/{}".format(photo.filename))
		return "Sucessfully uploaded!"


if __name__ == "__main__":
	app.run(debug=True, port=8000)