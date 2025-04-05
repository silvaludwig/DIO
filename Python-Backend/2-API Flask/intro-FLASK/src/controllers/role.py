from flask import Blueprint, request
from src.app import db, Role
from http import HTTPStatus


app = Blueprint('role', __name__, url_prefix="/roles")

@app.route('/', methods=["POST"])
def create_role():
    if request.method == "POST":
        data = request.json
        role = Role(name=data['name'])
        db.session.add(role)
        db.session.commit()
        return {"message": "created Role"}, HTTPStatus.CREATED