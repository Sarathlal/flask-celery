from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plugin(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(150))
   version = db.Column(db.String(10))

def __init__(self, name, version):
   self.name = name
   self.version = version