import pymongo
import datetime
import os

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client[os.getenv("DB_NAME")]

class Post:

    def __init__(self, title, author, tags, content):
        posts_list= db.posts.find()

        if posts_list == []:
            self.id= 1
        else:
            self.id= list(db.posts.find())[-1]["id"]+1
        
        self.created_at= datetime.datetime.utcnow()
        self.updated_at= ""
        self.title= title
        self.author= author
        self.tags= tags
        self.content= content

    @staticmethod
    def read_posts():
        posts_list= list(db.posts.find())
        jsonified_posts_list= []

        for post in posts_list:
            post.pop("_id")
            jsonified_posts_list.append(post)

        return jsonified_posts_list

    @staticmethod
    def read_post_by_id(id):
        post= db.posts.find_one({"id": id})
        post.pop("_id")

        return post

    @staticmethod
    def create_post(data):
        db.posts.insert_one(data)
        post = db.posts.find_one({"id": data["id"]})
        post.pop("_id")
        return post

    @staticmethod
    def delete_post(id):
        post = db.posts.find_one({"id": id})
        post.pop("_id")
        db.posts.delete_one({"id": id})

        return post

    @staticmethod
    def update_post(data, id):
        data["updated_at"]= datetime.datetime.utcnow()

        update = {"$set": data}
        post= db.posts.find_one({"id": id})

        db.posts.update_one(post, update)

        new_post= db.posts.find_one({"id": id})
        new_post.pop("_id")

        return new_post
