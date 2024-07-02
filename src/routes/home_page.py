from src.models import *
from flask import jsonify, request
from src.schemas import userSchema,UserSchemas
from src.models import User
from datetime import datetime,timedelta
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


bcrypt = Bcrypt()
@jwt_required()
def home_page():
    try:
        users = User.query.all()
        if users:
            result = UserSchemas.dump(users)
            return jsonify({"success":True, "message":"User found","data":result})
        else:
            return {"success":False,"message":"Products not found"}
    except Exception as ex:
        return ex


def registerUser():
    try:
        email           = request.json['email']
        name            = request.json['name']
        last_name       = request.json['last_name']
        phone           = request.json['phone']
        image           = request.json['image']
        password        = request.json['password']
        is_available    = request.json.get('is_available', True)
        
        
        # Obtener la fecha y hora actual en formato ISO 8601
        current_datetime_iso = datetime.now().isoformat()

        # Si created_at y updated_at no se envían en la solicitud, usar la fecha actual
        created_at_str = request.json.get('created_at', current_datetime_iso)
        updated_at_str = request.json.get('updated_at', current_datetime_iso)
        
        # Convertir las cadenas de fecha a objetos datetime
        created_at = datetime.fromisoformat(created_at_str)
        updated_at = datetime.fromisoformat(updated_at_str)

        # Encriptar contraseña
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        #hashed_password = generate_password_hash(password)

        new_user = User(
            email=email,
            name=name,
            last_name=last_name,
            phone=phone,
            image=image,
            password=hashed_password,
            is_available=is_available,
            session_token=create_access_token(identity={'email':email},expires_delta=timedelta(minutes=120)),
            created_at=created_at,
            updated_at=updated_at
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"success": True, "message": "User saved successfully"})
    except ValueError as ve:
        return jsonify({"success": False, "message": str(ve)})
    except Exception as ex:
        return jsonify({"success": False, "message": f"An error occurred: {str(ex)}"})


def login_user():
    email      = request.json['email']
    password   = request.json['password']
    try:
        user = User.query.filter_by(email = email).first()
        if user.email:
            password_hash = user.password
            user_found = userSchema.dump(user)
            if bcrypt.check_password_hash(password_hash,password):
                return jsonify({"success": True, "message": "User Logged", "data":[user_found]})
            else:
                return jsonify({"success": True, "message": "Password Incorrect"})
        else:
            return jsonify({"success": True, "message": "User No Found"})
    except ValueError as ve:
        return jsonify({"success": False, "message": str(ve)})