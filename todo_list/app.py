from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.66.73:3306/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default=False)

@app.route("/")
def index():
    return "This is a TODO app"

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')