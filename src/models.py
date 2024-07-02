from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id              = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email           = db.Column(db.String(100), unique=True, nullable=False)
    name            = db.Column(db.String(100), nullable=False)
    last_name       = db.Column(db.String(100), nullable=False)
    phone           = db.Column(db.String(80), unique=True, nullable=False)
    image           = db.Column(db.String(255))
    password        = db.Column(db.String(100), nullable=False)
    is_available    = db.Column(db.Boolean)
    session_token   = db.Column(db.String(512))
    created_at      = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at      = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, email, name, last_name, phone, image, password, is_available, session_token, created_at, updated_at):
        self.email          = email
        self.name           = name
        self.last_name      = last_name
        self.phone          = phone
        self.image          = image
        self.password       = password
        self.is_available   = is_available
        self.session_token  = session_token
        self.created_at     = created_at
        self.updated_at     = updated_at
