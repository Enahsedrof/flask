from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.197.238.11/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "ererhe"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default=False)

class TodoForm(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("Add Todo")

@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST","GET"])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(task=form.task.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')