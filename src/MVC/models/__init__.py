from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    """
    init
    """
    db.create_all()