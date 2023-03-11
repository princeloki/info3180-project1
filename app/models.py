from . import db

class PropertiesProfile(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    no_bedrooms = db.Column(db.Integer)
    no_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Integer())
    type = db.Column(db.String(20))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(255))
    
    def __init__(self,title, no_bedrooms, no_bathrooms, location, price, type, description, photo):
        self.title = title
        self.no_bedrooms = no_bedrooms
        self.no_bathrooms = no_bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo
