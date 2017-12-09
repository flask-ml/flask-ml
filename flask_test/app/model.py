from hashlib import md5
from sqlalchemy import Table, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, or_, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

Base = declarative_base()
URL = 'sqlite:///tmp/user.db'
engine = create_engine(URL)
Session = scoped_session(sessionmaker(bind=engine))

class User(Base):
	__tablename__ = 'user'

	email = Column(String(50), primary_key = True)
	name = Column(String(50), nullable = False)
	pw = Column(String(50), nullable = False)

	def __repr__(self):
		return "<user.name = %r>" % self.name


def classToDict(obj):
	if obj is None:
		return None

	is_list = obj.__class__ == [].__class__
	is_set = obj.__class__ == set().__class__

	if is_list or is_set:
		obj_arr = []
		for o in obj:
			dict = {}
			dict.update(o.__dict__)
			obj_arr.append(dict)
		return obj_arr
	else:
		dict = {}
		dict.update(obj.__dict__)
		return dict

from contextlib import contextmanager
@contextmanager
def session_scope():
	"""
	创建上下文管理，处理事务，操作失败回滚
	"""
	session = Session()
	try:
		yield session
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()


def query_user(name = None):
	with session_scope() as session:
		return session.query(User).filter(User.name == name).first()

def add_user(email, name, pw):
	with session_scope() as session:
		user = User(name=name,email=email,
		pw=pw)
		session.add(user)
		
# Base.metadata.create_all(engine)
# add_user('2@email.com', 'haha', '1')