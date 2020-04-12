from flask import Blueprint, jsonify, request, abort, Response
from http import HTTPStatus
from app import mongo

bp = Blueprint("api", __name__)

@bp.route('/')
def index():
    return jsonify({'greeting': 'Hello World!!!'})

@bp.route('/users/register', methods=['POST'])
def registerUser():
    if mongo.db.users.find_one({"email": request.json['email']}) != None:
        abort(HTTPStatus.CONFLICT)
    mongo.db.users.insert({"name": request.json['name'], "email": request.json['email']})
    return jsonify(), HTTPStatus.CREATED

@bp.route('/users', methods=['GET'])
def getAllUsers():
    users = mongo.db.users.find()
    return jsonify([{"name": user['name'], "email": user['email']} for user in users])

@bp.route('/users/<email>', methods=['GET'])
def getUser(email):
    user = mongo.db.users.find_one_or_404({"email": email})
    return jsonify({"name": user['name'], "email": user['email']})

@bp.route('/users/<email>', methods=['DELETE'])
def deleteUser(email):
    mongo.db.users.find_one_or_404({"email": email})
    mongo.db.users.delete_one({"email": email})
    return jsonify()