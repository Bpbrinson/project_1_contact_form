from flask_sqlalchemy import SQLAlchemy

# Initialize DB instance
db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name