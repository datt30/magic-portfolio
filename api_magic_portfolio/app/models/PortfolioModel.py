from app import db


class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    idportfolio = db.Column(db.Integer, primary_key=True)
    twitter_user_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    names = db.Column(db.String(255))
    last_names = db.Column(db.String(255))

    def __init__(self, idportfolio, twitter_user_name, description, image_url, title, names, last_names):
        self.idportfolio = idportfolio
        self.twitter_user = twitter_user_name
        self.description = description
        self.image_url = image_url
        self.title = title
        self.names = names
        self.last_names = last_names

    def serialize(self):
        return {
            'idPortfolio': self.idportfolio,
            'twitterUser': self.twitter_user_name,
            'description': self.description,
            'imageUrl': self.image_url,
            'title': self.title,
            'names': self.names,
            'lastNames': self.last_names
        }
