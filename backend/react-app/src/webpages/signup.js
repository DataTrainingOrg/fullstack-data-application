from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:psw@localhost/test_json'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_info = db.Column(db.PickleType)

    def __repr__(self):
        return self.user_info


class Students(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), unique=True)
    student_age = db.Column(db.Integer)
    student_sex = db.Column(db.String(20))

    def to_json(self):
        json_student = {
            'student_id': self.student_id,
            'student_name': self.student_name,
            'student_sex': self.student_sex,
            'student_age': self.student_age
        }

        return json_student

    def __repr__(self):
        return '%r' % self.student_id