from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'last_name', 'phone', 'image', 'password', 'is_available', 'session_token', 'created_at', 'update_at')
	
userSchema  = UserSchema()
UserSchemas = UserSchema(many=True)