from bottle import Bottle, run, template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean

# On crée le lien vers la base de données
DB_URI = 'mysql+pymysql://myuser:mypassword@localhost/mydatabase'
engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# On crée la table TodoList
class TodoList(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(100), nullable=False)
    # Ressort comme un Tinyint de 0 ou 1
    status = Column(Boolean, nullable=False, default=False)


Base.metadata.create_all(engine)

# On crée l'appel de l'application Bottle
app = Bottle()


# On crée les différentes routes.
@app.route('/todo')
def todo_list():
    validate_todo = get_validate_todo()
    unvalidate_todo = get_unvalidate_todo()
    todos = session.query(TodoList).all()
    return template('views/todo_list_template', todos=todos, validate_todo=validate_todo, unvalidate_todo=unvalidate_todo)


@app.route('/todo/add', method='POST')
def add_todo():
    task = request.forms.get('task')
    new_todo = TodoList(task=task, status=False)
    session.add(new_todo)
    session.commit()
    return redirect('/todo')


@app.route('/todo/update/<id:int>', method='POST')
def update_todo(id):
    status = request.forms.get('status') == 'on'
    todo = session.query(TodoList).get(id)
    todo.status = status
    session.commit()
    return redirect('/todo')


def get_validate_todo():
    validate_task = 0
    todos = session.query(TodoList).all()
    for todo in todos:
        if todo.status:
            validate_task += 1
    return validate_task


def get_unvalidate_todo():
    unvalidate_task = 0
    todos = session.query(TodoList).all()
    for todo in todos:
        if not todo.status:
            unvalidate_task += 1
    return unvalidate_task


@app.route('/todo/all_task')
def get_all_todo():
    validate_todo = get_validate_todo()
    unvalidate_todo = get_unvalidate_todo()
    total_todo = validate_todo + unvalidate_todo
    return template('views/todo_numbers_template', validate_todo=validate_todo, unvalidate_todo=unvalidate_todo, total_todo=total_todo)


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
