# let's import the flask

import os
from flask import Flask,  Response, request
import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)

mongoDB_url = "mongodb+srv://myself:321123@python.aqlmxar.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongoDB_url)
db = client.thirty_days_of_python


@app.route('/api/v1.0/students', methods=['GET'])
def students():
    student_list = [
        {
            'name': 'Asabeneh',
            'country': 'Finland',
            'city': 'Helsinki',
            'skills': ['HTML', 'CSS', 'JavaScript', 'Python']
        },
        {
            'name': 'David',
            'country': 'UK',
            'city': 'London',
            'skills': ['Python', 'MongoDB']
        },
        {
            'name': 'John',
            'country': 'Sweden',
            'city': 'Stockholm',
            'skills': ['Java', 'C#']
        }
    ]
    student = db.students.find()
    return Response(dumps(student), mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find({'_id': ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')


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
    return


@app.route('/api/v1.0/students/<id>', methods=["PUT"])
def update_student(id):
    query = {'_id': ObjectId(id)}
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
    db.students.update_one(query, student)
    return


@app.route('/api/v1.0/students/<id>', methods=["DELETE"])
def delete_student(id):
    query = {"_id": ObjectId(id)}
    db.students.delete_one(query)
    return


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
