from flask import Flask, render_template, redirect, request, url_for, Response
import os
import ast
import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
app = Flask(__name__)

mongoDB_url = "mongodb+srv://myself:321123@python.aqlmxar.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongoDB_url)
db = client.thirty_days_of_python


@app.route('/')
def home():
    frontend = ['HTML', 'CSS', 'JavaScript']
    backend = ["Python", "Flask", "MongoDB"]
    name = '30 Days Of Python Programming'
    return render_template('home.html', frontend=frontend, backend=backend, name=name, title="Home")


@app.route("/about")
def about():
    name = '30 Days Of Python Programming'
    return render_template('about_us.html', name=name, title='About Us')


@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'GET':
        student = db.students.find()
        list_stud = list(student)
        return render_template('students.html', students=list_stud)


@app.route('/students/update/<id>', methods=['GET', 'POST'])
def update_student_d(id):
    if request.method == 'GET':
        student = db.students.find({'_id': ObjectId(id)})
        stud = list(student)
        return render_template('update_student.html', student=stud, id=id)


@app.route('/api/v1.0/students/update/<id>', methods=["POST"])
def update_student(id):
    query = {'_id': ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {"$set": {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }}
    db.students.update_one(query, student)
    return redirect(url_for('students'))


@app.route('/api/v1.0/students/<id>', methods=["POST"])
def delete_student(id):
    query = {"_id": ObjectId(id)}
    db.students.delete_one(query)
    return redirect(url_for('students'))


@app.route('/result')
def result():
    data = request.args.to_dict()
    headers = ["WORD", "WORD COUNT"]
    tableData = request.args.getlist("words")
    table = [i for i in ast.literal_eval(tableData[0])]
    return render_template('result.html', data=data, headers=headers, tableData=sorted(table, reverse=True))


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        text = content.lower().split()
        num_of_char = len(content)
        total_words = len(text)
        freq_words = [(text.count(x), x) for x in text]
        freq_word = (max(freq_words, key=lambda x: x[0]))[1]
        word_variety = (len(set(freq_words)) / total_words * 100)
        data = {"num_of_char": num_of_char,
                "total_words": total_words, "freq_word": freq_word, "word_variety": "{:.1f}".format(word_variety)}
        return redirect(url_for('result', **data, words=set(freq_words)))


@app.route("/api/v1.0/students", methods=["GET"])
def list_student():
    student = db.students.find()
    return Response(dumps(student), mimetype='application/json')


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    name = '30 Days Of Python Programming'
    if request.method == 'GET':
        return render_template('add_students.html', name=name, title=name)
    if request.method == 'POST':
        return redirect(url_for('create_student'))


@app.route('/api/v1.0/students', methods=["POST"])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()

    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    db.students.insert_one(student)
    return redirect(url_for('students'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
