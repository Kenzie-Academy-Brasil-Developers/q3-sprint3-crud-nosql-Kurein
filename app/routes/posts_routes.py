from http import HTTPStatus
from flask import Flask, jsonify, request
from app.models import Post
from app.controller import create_post_controller

def posts_routes(app: Flask):

    @app.post('/posts')
    def create_post():
        data = request.get_json()
        try:
            return jsonify(create_post_controller(data)), HTTPStatus.CREATED
        except TypeError:
            return {'error': 'key missing'}, HTTPStatus.BAD_REQUEST

    @app.get('/posts')
    def read_posts():
        return jsonify(Post.read_posts()), HTTPStatus.OK

    @app.get('/posts/<post_id>')
    def read_post_by_id(post_id):
        try:
           return jsonify(Post.read_post_by_id(int(post_id))), HTTPStatus.OK
        except AttributeError:
            return {'error': 'id non existant'}, HTTPStatus.NOT_FOUND
        

    @app.patch('/posts/<post_id>')
    def update_post(post_id):
        data = request.get_json()
        try:
            return jsonify(Post.update_post(data, int(post_id))), HTTPStatus.OK
        except TypeError:
            return {'error': 'id non existant'}, HTTPStatus.NOT_FOUND
    
    @app.delete('/posts/<post_id>')
    def delete_post(post_id):
        try:
            return jsonify(Post.delete_post(int(post_id))), HTTPStatus.OK
        except AttributeError:
            return {'error': 'id non existant'}, HTTPStatus.NOT_FOUND