import os

from flask import Flask ,request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Namespace, Resource, fields
from models import User, TertiaryApplication ,db
from flask_migrate import Migrate
from flask_cors import CORS
import secrets
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from jwt.exceptions import ExpiredSignatureError, DecodeError
import jwt
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

# postgres://masingabackend_user:DUGhDP54CzfWQereBjumF0jqriPcsQEW@dpg-cm29kita73kc738kvlcg-a.oregon-postgres.render.com/masingabackend
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

CORS(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-RESTx
api = Api()
api.init_app(app)

# Define API namespace
ns = Namespace('bursarymanagement')
api.add_namespace(ns)
#---------#
jwt = JWTManager(app)

# --------------------------schemas------------------------------------
tertiaryapplicationschema = api.model('tertiaryapplication', {
    'id' : fields.Integer,
    'Fullname': fields.String(required=True, description='Name of the item'),
    'Gender': fields.String(description='Description of the item'),
    'Nationalid': fields.String(description='URL of the item image'),
    'GuardiansNo': fields.String(description='User ID reporting the item') ,
    'Motherid' : fields.String,
    'Disability' : fields.String ,
    'Ward' : fields.String ,
    'Location' : fields.String ,
    'Sublocation' : fields.String ,
    'Village' : fields.String ,
    'Institution' : fields.String ,
    'Admno' : fields.String , 
    'Modeofstudy' : fields.String ,
    'Yearofstudy' : fields.String ,
    'Semester'  : fields.String ,
    'Coarseduration' : fields.String ,
    'Family' : fields.String ,
    'Fathersincome' : fields.String ,
    'Mothersincome' : fields.String ,
    'Approvalstatus' : fields.String ,
})

user_login_schema =api.model('login' , {
   'Nationalid' : fields.Integer,
})

admin_login_schema =api.model('login' , {
   'Phonenumber' : fields.Integer ,
   'password' : fields.String ,
})

#--------------------------------------end of schemas---------------------------------------
@ns.route('/tertiaryapplication')
class PostItemlost(Resource):
    @ns.expect(tertiaryapplicationschema)
    def post(self):
        try:
            data = request.json  # Get the JSON data from the request

            #check whether fields are missing
            fullname = data.get('fullname')
            gender = data.get('gender')
            phonenumber = data.get('phonenumber')
            nationlid = data.get('nationid')
            guardiansNo = data.get('guardiansno')
            mothersid = data.get('mothersid')
            disability = data.get('disability')
            ward = data.get('ward')
            location = data.get('location')
            sublocation = data.get('sublocation')
            village = data.get('village')
            institution = data.get('institution')
            admno = data.get('admno')
            levelofstudy = data.get('levelofstudy')
            modeofstudy = data.get('modeofstudy')
            yearofstudy = data.get('yearofstudy')
            semester = data.get('semester')
            coarseduration = data.get('coarseduration')
            family = data.get('family')
            fathersincome = data.get('fathersincome')
            mothersincome = data.get('mothersincome')
            approvalstatus = data.get('approvalstatus')

        
            new_application = TertiaryApplication(
                
         Fullname = fullname ,
         Gender = gender,
         Nationalid = nationlid ,
         Phonenumber = phonenumber ,
         GuardiansNo = guardiansNo ,
         Motherid = mothersid ,
         Disability = disability,
         Ward = ward ,
         Location = location,
         Sublocation = sublocation ,
         Village = village ,
         Instituition = institution ,
         Admno = admno ,
         levelofstudy = levelofstudy ,
         Modeofstudy = modeofstudy,
         Yearofstudy = yearofstudy ,
         Semester = semester,
         Coarseduration = coarseduration ,
         Family = family ,
         Fathersincome = fathersincome ,
         Mothersincome = mothersincome ,
         Approvalstatus = approvalstatus
            )

            db.session.add(new_application)
            db.session.commit()


            # Create a new user entry
            new_user = User(
                Nationalid = nationlid,
                Phonenumber = phonenumber,
            )

            db.session.add(new_user)
            db.session.commit()

            return {
                "message": "Application created successfully",
                "application": {
                    "fullname": new_application.Fullname,
                    "Gender": new_application.Gender,
                    "Nationalid": new_application.Nationalid,
                    "GuardiansNo": new_application.GuardiansNo,
                    'Mothersid': new_application.Motherid,
                    'Disability' : new_application.Disability ,
                    'Ward' : new_application.Ward ,
                    'Approvalstatus' : new_application.Approvalstatus
                }
            }, 201

        except Exception as e:
            db.session.rollback()
            return {
                "message": "Failed to create an application",
                "error": str(e)
            }, 500

# login as student
    @ns.route('/login')
    class Login(Resource):
        @ns.expect(user_login_schema)
        def post(self):
            data = request.get_json()
            # check whether data is missing 
            nationalid = data.get('Nationalid')
          
            if not(nationalid):
                return{
                    'message': 'Missing nationalid'
                } , 400
            
            # query to database to find the user with the provided username
            user = User.query.filter_by(Nationalid=nationalid).first()
            if not user:
                return {
                    'message' : 'could Not Verify'
                } , 401
            
           
            return {
                'id' : user.Nationalid ,
                'Role' : user.Role
            } , 201
        
#adminlogin
@ns.route('/loginadmin')
class Adminlogin(Resource):
    @ns.expect(admin_login_schema)
    def post(self):
        data = request.get_json()
        # check whether data is missing or if the username or 'password' are missing
        phonenumber = data.get('Phonenumber')
        password = data.get('password')
        if not(phonenumber and password):
            return{
                'message': 'Missing username , password'
            } , 400
        
        # query to database to find the user with the provided phonenumber
        user = User.query.filter_by(Phonenumber = phonenumber).first()
        if not user:
            return {
                'message' : 'could Not Verify'
            } , 401
        
        return {
            'nationalid' : user.Nationalid 
        } , 201
        

#fetch by id
@ns.route('/mydetails/<string:nationalid>')
class Users(Resource):
    @ns.marshal_list_with(tertiaryapplicationschema)  # Assuming get_lostitems_schema is used for marshaling individual items
    def get(self , nationalid):
        applicationdetails = TertiaryApplication.query.filter_by(Nationalid= nationalid).all()
        if not applicationdetails:
            # You can customize the response if no lost items are found
            return {"message": "No such application found"}, 404
        return applicationdetails, 200

#fetch all application
@ns.route('/allapplication')
class Users(Resource):
    @ns.marshal_list_with(tertiaryapplicationschema)
    def get(self):
        users = TertiaryApplication.query.all()
        return users, 200
    
#fetch by ward
@ns.route('/allapplication/<string:wardname>')
class UsersByWard(Resource):
    @ns.marshal_list_with(tertiaryapplicationschema)
    def get(self, wardname):
        users = TertiaryApplication.query.filter_by(Ward=wardname).all()
        if not users:
            return {"message": f"No applications found for Ward: {wardname}"}, 404
        return users, 200

#ApproveBursary
@ns.route('/approveBursaryapplication/<int:item_id>')
class ApproveBursaryApplication(Resource):
    def put(self, item_id):
        application = TertiaryApplication.query.get(item_id)

        if application and application.Approvalstatus == 'Notapproved':
            application.Approvalstatus = 'Approved'
            db.session.commit()
            return {"message": "Application approved by admin"}, 200
        else:
            return {"error": "Application not approved "}, 404

    