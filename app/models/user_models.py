# Authors: Jose Enrique Ruiz Navarro <joseenriqueruiznavarro@gmail.com>

from app import db,ma


# Define the User data model. !
class User(db.Model):
    __tablename__ = 'model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255))
    age = db.Column(db.Integer)

    # User authentication information (required for Flask-User)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)


# Define the User metadata model to serialize !
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","name","age", "email")

