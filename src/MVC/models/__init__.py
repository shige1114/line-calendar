from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init():
    """
    init
    """
    db.create_all()