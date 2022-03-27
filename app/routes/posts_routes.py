from http import HTTPStatus
from flask import Flask, jsonify, request
from app.models import Post
from app.controller import create_post_controller

def posts_routes(app: Flask):

    @app.post('/posts')
    def create_post():
        data = request.get_json()
        return jsonify(create_post_controller(data)), HTTPStatus.CREATED

    @app.get('/posts')
    def read_posts():
        return jsonify(Post.read_posts()), HTTPStatus.OK

    @app.get('/posts/<post_id>')
    def read_post_by_id(post_id):
        return jsonify(Post.read_post_by_id(int(post_id))), HTTPStatus.OK

    @app.patch('/posts/<post_id>')
    def update_post(post_id):
        data = request.get_json()
        return jsonify(Post.update_post(data, int(post_id))), HTTPStatus.OK
    
    @app.delete('/posts/<post_id>')
    def delete_post(post_id):
        return jsonify(Post.delete_post(int(post_id))), HTTPStatus.OK