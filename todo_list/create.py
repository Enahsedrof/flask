from app import db, Todo

db.drop_all()
db.create_all()

test_task = Todo(task='First task',complete= True) # Extra: this section populates the table with an example entry
db.session.add(test_task)
db.session.commit()
