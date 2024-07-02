import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:@localhost/appDelivery'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #hernan
    #JWT_SECRET_KEY = '$2a$20$i6.bcop3d5XfDvEsDYLqTu05mMw95ZWe0eW4r69DAE7PsVUfpZpDS'