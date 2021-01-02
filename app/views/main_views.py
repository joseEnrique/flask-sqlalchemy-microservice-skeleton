# Authors: Jose Enrique Ruiz Navarro <joseenriqueruiznavarro@gmail.com>

from flask import Blueprint, request,jsonify

from app import db
from app.models.user_models import User, UserSchema

main_blueprint = Blueprint('main', __name__)


# The root page is accessible to anyone
@main_blueprint.route('/')
def root_page():
    return "hello world"


@main_blueprint.route('/users', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        if 'id' not in request.json or 'email' not in request.json:
            return jsonify(request.json), 403
        user_posted = User(id=request.json['id'], email=request.json['email'])
        db.session.add(user_posted)
        db.session.commit()
        return UserSchema().dump(user_posted)
    if request.method == 'GET':
        users = User.query.all()
        result = UserSchema(many=True).dump(users)
        return jsonify(result)

