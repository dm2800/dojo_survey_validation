from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash


class Dojo: 
    db = "dojo_survey_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,location,language,comment,created_at,updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query,data)
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1: 
            return False
        return cls(results[0])


    @staticmethod
    def validate_dojo(dojo):
        is_valid = True 
        if len(dojo['name']) < 1:
            flash("Name is a required field.")
            is_valid = False
        if len(dojo['location']) < 1: 
            flash("Location is a required field.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Language is a required field.")
            is_valid = False
        if len(dojo['comment']) < 3 :
            flash("Comment is a required field.")
            is_valid = False 
        return is_valid 
