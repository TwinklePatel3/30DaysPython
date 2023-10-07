from bson import ObjectId
from flask import Flask, render_template
import os
import pymongo
mongoDB_url = "mongodb+srv://myself:321123@python.aqlmxar.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongoDB_url)
db = client.thirty_days_of_python
# db.students.insert_one(
#     {"name": "Twinkle", "country": "India", "city": "Mumbai", "age": 22})
# print(client.list_database_names())
# students = [
#     {'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34},
#     {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
#     {'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25},
# ]
# for student in students:
#     db.students.insert_one(student)
# students = db.students.find_one({'_id': ObjectId('650f15a198e47e926ad233d3')})
# students = db.students.find()
# 0 means not include and 1 means include
# students = db.students.find({}, {"_id": 0,  "name": 1, "country": 1})
# query = {
#     # "country": "UK",
#     # "city": "London"
#     "age": {"$gte": 25}
# }
query = {"age": 22}
new_value = {"$set": {"age": 23}}
# students = db.students.find(query)
# students = db.students.find().sort("name")
# students = db.students.find().sort("age", -1)
# db.students.update_one(query, new_value)
db.students.delete_one({"name": "Twinkle"})
students = db.students.find()
for student in students:
    print(student)

# db.students.drop()

app = Flask(__name__)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
