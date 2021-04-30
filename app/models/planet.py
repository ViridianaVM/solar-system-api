#This db should be the same as in app/__init__.py >> db = SQLAlchemy() <<
from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    __tablename__ = "planets"

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


    def to_string(self):
        return f"{self.id}: {self.name} Description: {self.description}"
