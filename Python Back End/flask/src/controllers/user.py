from http import HTTPStatus

from flask import Blueprint , request
from sqlalchemy import inspect
from app import User , db
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

app = Blueprint('user' , __name__ , url_prefix='/users')

def _create_user():
    data = request.json
    user = User(
         username = data["username"],
         username = data["password"],
         username = data["role_id"])
    db.session.add(user)
    db.session.commit()


def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            'id': user.id,
            'username': user.username
        }
        for user in users
    ]

# localhost:5000/users
@app.route('/',methods = ['GET','POST'])
@jwt_required()
def list_or_create_user():
    if request.method == 'POST':
        _create_user()
        return {"message" : "User created!" } , HTTPStatus.CREATED
    else :
        return{"identity":get_jwt_identity() ,"users" : _list_users()}
    
@app.route('/<int:user_id>')
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
            'id': user.id,
            'username': user.username
        }
    
@app.route('/<int:user_id>' , methods = ['PATCH'])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    mapper = inspect(User)
    for column in mapper.attrs:
            if column.key in data:
                 setattr(user,column.key , data[column.key])
 
    return {
            'id': user.id,
            'username': user.username
        }

@app.route('/<int:user_id>' , methods = ['DELETE'])
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return '' , HTTPStatus.NO_CONTENT