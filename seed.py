""" Seed file for sample db data """
from models import db, User, Post
from app import app
from datetime import date, datetime

now = datetime.now()

db.drop_all()
db.create_all()

q = User(username='Q',
             first_name='quentin',
             last_name='williams')
maddy = User(username='maddy',
             first_name='madison',  
             last_name='weidman')
milly = User(username='millybean',
             first_name='Millikan',
             last_name='Williams')
willy = User(username='willybean',
             first_name='Willow',
             last_name='Williams')
post1 = Post(title='first',
             content='this is the first post',
             date_created=now
             )
post2 = Post(title='title only',
             date_created=now)

db.session.add_all([q, maddy, milly, willy])
db.session.commit()



db.session.add(post1)
db.session.add(post2)
db.session.commit()