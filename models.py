from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    inventory_number = db.Column(db.String(64), unique=True, nullable=False)
    category = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(32), nullable=False, default='рабочее')
    purchase_date = db.Column(db.String(10))   # YYYY-MM-DD
    location = db.Column(db.String(128))
