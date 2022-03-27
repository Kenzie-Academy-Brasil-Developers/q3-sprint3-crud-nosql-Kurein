from app.models import Post

def create_post_controller(data):
    post = Post(**data)
    
    return Post.create_post(post.__dict__)
