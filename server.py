from flask import Flask, request, jsonify, make_response, render_template, Blueprint
from flask_restful import Api
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from config import app, api, mysql
from resources.Register import Register
from resources.Login import Login
from resources.UserExists import UserExists
from resources.ClassifyEmotion import ClassifyEmotion
from resources.ResetPassword import ResetPassword
from resources.UserInfo import UserInfo
from resources.PhotoDescription import PhotoDescription
from resources.EmotionsQuery import EmotionsQuery
from resources.PhotoUri import PhotoUri
from resources.PhotoTag import PhotoTag
from resources.AdminQuery import AdminQuery
from resources.AdminQuery2 import AdminQuery2
from resources.EditEmotions import EditEmotions
from resources.IsAdmin import IsAdmin

api.add_resource(Register, '/Register')
api.add_resource(UserExists, '/UserExists')
api.add_resource(Login, '/Login')
api.add_resource(ClassifyEmotion, '/ClassifyEmotion')
api.add_resource(ResetPassword, '/ResetPassword')
api.add_resource(UserInfo, '/UserInfo')
api.add_resource(PhotoDescription, '/PhotoDescription')
api.add_resource(EmotionsQuery, '/EmotionsQuery')
api.add_resource(PhotoTag, '/PhotoTag')
api.add_resource(PhotoUri, '/PhotoUri')
api.add_resource(AdminQuery, '/AdminQuery')
api.add_resource(AdminQuery2, '/SplAdminQuery')
api.add_resource(EditEmotions, '/EditEmotions')
api.add_resource(IsAdmin, '/IsAdmin')


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def handle_error(e):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def handle_error(e):
    return make_response(jsonify({'error': 'Internal server error'}), 500)

@app.errorhandler(403)
def handle_error(e):
    return make_response(jsonify({'error': 'Unauthorized'}), 403)



if __name__ == '__main__':
    app.run()
