from flask import Flask, request
from pymongo import MongoClient
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
url = ''
cluster = MongoClient(url)
db = cluster['fall2021']

@application.route('/')
def get_home():
    return "root"


@application.route('/courses/')
def get_courses():
    departments = request.args.getlist('deps[]')
    course_list = []
    for dep in departments:
        results = db[dep].find({})
        for res in results:
            course_list.append(res)
    course_list = sorted(course_list, key=lambda k: k['nugget'])
    return {'data': course_list}



if __name__ == "__main__":
    application.run()
