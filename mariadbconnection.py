from bottle import Bottle, route, run, template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean

DB_URI = 'mysql+pymysql://myuser:mypassword@localhost/mydatabase'
engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class TodoList(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(100), nullable=False)
    status = Column(Boolean, nullable=False, default=False)


Base.metadata.create_all(engine)

# conn = engine.connect()
# conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
# conn.commit()


# @route('/todo')
# def todo_list():
#     c = conn.cursor()