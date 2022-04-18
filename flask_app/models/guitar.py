from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "project"


class Guitar:
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.price = data['price']
        self.color = data['color']
        self.orientation = data['orientation']
        self.image = data['image']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO guitars (make,model,price,color,orientation,image,user_id)
                VALUES (%(make)s, %(model)s, %(price)s, %(color)s,%(orientation)s, %(image)s,%(user_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM guitars WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM guitars;"""
        results = connectToMySQL(db).query_db(query)
        guitars = []
        for row in results:
            guitars.append(cls(row))
        return guitars

    # @classmethod
    # def update(cls, data):
    #     query = """
    #             UPDATE guitars SET make=%(make)s, model=%(model)s, price=%(price)s, color=%(color)s,
    #             orientation=%(orientation)s, image=%(image)s,updated_at=NOW() WHERE id = %(id)s;
    #             """
    #     return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = """
                DELETE FROM guitars WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate(guitar):
        is_valid = True
        if guitar['music_style'] == "":
            flash("Please select a music style", "guitar")
            is_valid = False
        if guitar['budget'] == "":
            flash("Please select a budget", "guitar")
            is_valid = False
        if guitar['looks'] == "":
            flash("Please select looks", "guitar")
            is_valid = False
        if guitar['orientation'] == "":
            flash("Please select orientatiom", "guitar")
            is_valid = False
        return is_valid
