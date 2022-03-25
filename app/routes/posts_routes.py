from flask import Flask

def posts_routes(app: Flask):

    @app.post('/posts')
    def create_post():
        return {'msg': 'post created'}

    @app.get('/posts')
    def get_posts():
        return {'msg': 'got all posts'}

    @app.get('/posts/<post_id>')
    def add_serie(post_id):
        return {'msg': f'got post from if {post_id}'}

    @app.patch('/post')
    def patch_post():
        return {'msg': 'post patched'}
    
    @app.delete('/post')
    def delete_post():
        return {'msg': 'post deleted'}