from utils.db import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    doors = db.Column(db.Integer, nullable=False)
    is_favorite = db.Column(db.Boolean)
    photo = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    cylinder_capacity = db.Column(db.Float, nullable=False)
    velocity = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"Brand:('{self.brand}', '{self.model}')"

    def to_json(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'doors': self.doors,
            'is_favorite': self.is_favorite,
            'photo': self.photo,
            'color': self.color,
            'cylinder_capacity': self.cylinder_capacity,
            'velocity': self.velocity
        }
