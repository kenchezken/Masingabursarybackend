
from flask import Flask ,request , jsonify , send_from_directory , url_for
from werkzeug.utils import secure_filename
from flask_restx import Api, Namespace, Resource, fields
from models import User, TertiaryApplication ,db
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://masingabursarydb_user:8iEaXZtdu8GcJ5Ptf4dnsJn9cJdB8Ibr@dpg-ctlgrulumphs73da1f5g-a.oregon-postgres.render.com/masingabursarydb'

# postgres://masingabackend_user:DUGhDP54CzfWQereBjumF0jqriPcsQEW@dpg-cm29kita73kc738kvlcg-a.oregon-postgres.render.com/masingabackend
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = '/var/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




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
    'Firstname': fields.String(required=True, description='Name of the item'),
    'Middlename': fields.String(required=True, description='Name of the item') ,
    'Lastname': fields.String(required=True, description='Name of the item') ,
    'Phonenumber' :fields.String ,
    'Gender': fields.String(description='Description of the item'),
    'Nationalid': fields.String(description='URL of the item image'),
    'GuardiansNo': fields.String(description='User ID reporting the item') ,
    'Guardianid' : fields.String,
    'Disability' : fields.String ,
    'Ward' : fields.String ,
    'Location' : fields.String ,
    'Sublocation' : fields.String ,
    'Village' : fields.String ,
    'Chiefname' : fields.String ,
    'Chiefphonenumber' : fields.String ,
    'Assistantchiefname' : fields.String ,
    'Assistantchiefno' : fields.String , 
    
    'Instituition' : fields.String ,
    'University' :fields.String ,
    'Amountexpecting' : fields.String ,
    'Amountreceived' : fields.String ,
    'Admno' : fields.String , 
    'Levelofstudy' : fields.String , 
    'Modeofstudy' : fields.String ,
    'Yearofstudy' : fields.String ,
    'Semester'  : fields.String ,
    'Coarseduration' : fields.String ,
    'Family' : fields.String ,
    'Fathersincome' : fields.String ,
    'Mothersincome' : fields.String ,
    'Approvalstatus' : fields.String ,
    'Imageurl' : fields.String
})

user_login_schema =api.model('login' , {
   'Nationalid' : fields.String,
})

admin_login_schema =api.model('login' , {
   'Phonenumber' : fields.Integer ,
   'password' : fields.String ,
})

#--------------------------------------end of schemas---------------------------------------

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        image_url = {filename}
        return jsonify({'message': 'File uploaded successfully', 'Imageurl': image_url}), 200

    return jsonify({'error': 'Invalid file type'}), 400



@app.route('/uploads/<filename>', methods=['GET'])
def get_image(filename):

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@ns.route('/tertiaryapplication')
class PostItemlost(Resource):
    @ns.expect(tertiaryapplicationschema)
    def post(self):
        try:
            data = request.json  # Get the JSON data from the request

            print(data
                  )

            #check whether fields are missing
            firstname = data.get('Firstname')
            middlename = data.get('Middlename')
            lastname = data.get('Lastname')
            gender = data.get('Gender')
            phonenumber = data.get('Phonenumber')
            nationlid = data.get('Nationalid')
            guardiansNo = data.get('GuardiansNo')
            guardiansid = data.get('Guardianid')
            disability = data.get('Disability')
            ward = data.get('Ward')
            location = data.get('Location')
            sublocation = data.get('Sublocation')
            village = data.get('Village')
            chiefname = data.get('Chiefname')
            chiefphonenumber = data.get('Chiefphonenumber')
            assistantchiefname = data.get('Assistantchiefname')
            assistantchiefno = data.get('Assistantchiefno')
                                          
            institution = data.get('Instituition')
            university = data.get('University')
            amountexpecting = data.get('Amountexpecting')
            amountreceived = data.get('Amountreceived')
            admno = data.get('Admno')
            levelofstudy = data.get('Levelofstudy')
            modeofstudy = data.get('Modeofstudy')
            yearofstudy = data.get('Yearofstudy')
            semester = data.get('Semester')
            coarseduration = data.get('Coarseduration')
            family = data.get('Family')
            fathersincome = data.get('Fathersincome')
            mothersincome = data.get('Mothersincome')
            approvalstatus = data.get('Approvalstatus')
            image_url = data.get('Imageurl')

            existing_application = TertiaryApplication.query.filter_by(Nationalid=nationlid).first()
            
            if existing_application:
                return {
                    "message": "An application with this National ID already exists",
                    "application": {
                # You can return existing_application data if needed
                    }
                }, 409  # Using status code 409 for conflict


        
            new_application = TertiaryApplication(
                
         Firstname = firstname ,
         Middlename = middlename ,
         Lastname = lastname ,
         Gender = gender,
         Nationalid = nationlid ,
         Phonenumber = phonenumber ,
         GuardiansNo = guardiansNo ,
         Guardianid = guardiansid ,
         Disability = disability,
         Ward = ward ,
         Location = location,
         Sublocation = sublocation ,
         Village = village ,
         Chiefname = chiefname ,
         Chiefphonenumber = chiefphonenumber ,
         AssistantChiefname =assistantchiefname ,
         Assistantchiefno = assistantchiefno ,
         Instituition = institution ,
         University = university ,
         Amountexpecting = amountexpecting ,
         Amountreceived = amountreceived ,
         Admno = admno ,
         levelofstudy = levelofstudy ,
         Modeofstudy = modeofstudy,
         Yearofstudy = yearofstudy ,
         Semester = semester,
         Coarseduration = coarseduration ,
         Family = family ,
         Fathersincome = fathersincome ,
         Mothersincome = mothersincome ,
         Imageurl = image_url ,
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

            print (new_application.Imageurl)

            return {
                "message": "Application created successfully",
                "application": {
                    "firstname": new_application.Firstname,
                    "middlemen" : new_application.Middlename ,
                    "lastname" : new_application.Lastname ,
                    "Gender": new_application.Gender,
                    "Phonenumber" : new_application.Phonenumber ,
                    "Nationalid": new_application.Nationalid,
                    "GuardiansNo": new_application.GuardiansNo,
                    'Guardiansid': new_application.Guardianid,
                    'Disability' : new_application.Disability ,
                    'Ward' : new_application.Ward ,
                    'Location' : new_application.Location ,
                    'Sublocation' : new_application.Sublocation ,
                    'Village' : new_application.Village ,
                    'Chiefname' : new_application.Chiefname ,
                    'Chiefphonenumber' : new_application.Chiefphonenumber ,
                    'AssistantChiefname' : new_application.AssistantChiefname ,
                    'Assistantchiefno' : new_application.Assistantchiefno ,
                    'Instituition' : new_application.Instituition ,
                    'University' : new_application.University ,
                    'Amountexpecting' : new_application.Amountexpecting ,
                    'Amountreceived' : new_application.Amountreceived ,
                    'Admno' : new_application.Admno ,
                    'levelofstudy' : new_application.levelofstudy ,
                    'Modeofstudy' : new_application.Modeofstudy ,
                    'Yearofstudy' : new_application.Yearofstudy ,
                    'Semester' : new_application.Semester ,
                    'Coarseduration' :new_application.Coarseduration ,
                    'Family' : new_application.Family ,
                    'Fathersincome' : new_application.Fathersincome ,
                    'Mothersincome' : new_application.Mothersincome ,
                    'Approvalstatus' : new_application.Approvalstatus ,
                    'imageurl' : new_application.Imageurl
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


 
@ns.route('/<int:item_id>')
@ns.response(404, 'Item not found')
@ns.response(500, 'Internal Server Error')
class ItemResource(Resource):
    @ns.response(200, 'Item deleted successfully')
    def delete(self, item_id):

     try:
            # Find the item by ID
            student = TertiaryApplication.query.get(item_id)
            if not student:
                return {'message': 'Item not found'}, 404
            
            # Delete the item
            db.session.delete(student)
            db.session.commit()
            return {'message': f'Item with ID {item_id} deleted successfully'}, 200
     except Exception as e:
            return {'message': str(e)}, 500


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


@ns.route('/Tertiaryapplication/<int:application_id>')  # Use the item_id as a parameter in the URL
class UpdateApplication(Resource):

    @ns.expect(tertiaryapplicationschema)
    def put(self,application_id):
        try:
            # Attempt to retrieve the item with the given item_id
            application= TertiaryApplication.query.get(application_id)

            if application:
                data = request.json  # Get the JSON data from the request
                print(data)
                application.Firstname  = data.get('Firstname')                              
                application. Middlename = data.get('Middlename')
                application.Lastname = data.get('Lastname')
                application. Gender = data.get('Gender')
                application. Phonenumber   = data.get('Phonenumber')
                application.Nationalid = data.get('Nationalid')
                application.GuardiansNo = data.get('GuardiansNo')
                application.Guardianid = data.get('Guardiansid')
                application.Disability = data.get('Disability')
                application.Ward = data.get('Ward')
                application. Location = data.get('Location')
                application.Sublocation = data.get('Sublocation')
                application.Village = data.get('Village')
                application.Chiefname = data.get('Chiefname')
                application.Chiefphonenumber = data.get('Chiefphonenumber')
                application.AssistantChiefname = data.get('Assistantchiefname')
                application. Assistantchiefno  = data.get('Assistantchiefno')
                application.Instituition  = data.get('Instituition')
                application. University = data.get('University')
                application. Amountexpecting = data.get('Amountexpecting')
                application.Amountreceived  = data.get('Amountreceived')
                application.Admno   = data.get('Admno')
                application.levelofstudy  = data.get('Levelofstudy')
                application.Modeofstudy = data.get('Modeofstudy')
                application.Yearofstudy = data.get('Yearofstudy')
                application.Semester  = data.get('Semester')
                application.Coarseduration  = data.get('Coarseduration')
                application.Family  = data.get('Family')
                application.Fathersincome = data.get('Fathersincome')
                application.Mothersincome = data.get('Mothersincome')
              

                db.session.commit()

                return {
                    "message": f"Application with ID {application_id} updated successfully",
                    "lostitem": {
                    "firstname": application.Firstname,
                    "middlemen" : application.Middlename ,
                    "lastname" : application.Lastname ,
                    "Gender": application.Gender,
                    "Phonenumber" : application.Phonenumber ,
                    "Nationalid": application.Nationalid,
                    "GuardiansNo": application.GuardiansNo,
                    'Guardiansid': application.Guardianid,
                    'Disability' : application.Disability ,
                    'Ward' : application.Ward ,
                    'Location' : application.Location ,
                    'Sublocation' : application.Sublocation ,
                    'Village' : application.Village ,
                    'Chiefname' : application.Chiefname ,
                    'Chiefphonenumber' : application.Chiefphonenumber ,
                    'AssistantChiefname' : application.AssistantChiefname ,
                    'Assistantchiefno' : application.Assistantchiefno ,
                    'Instituition' : application.Instituition ,
                    'University' : application.University ,
                    'Amountexpecting' : application.Amountexpecting ,
                    'Amountreceived' : application.Amountreceived ,
                    'Admno' : application.Admno ,
                    'levelofstudy' : application.levelofstudy ,
                    'Modeofstudy' : application.Modeofstudy ,
                    'Yearofstudy' : application.Yearofstudy ,
                    'Semester' : application.Semester ,
                    'Coarseduration' :application.Coarseduration ,
                    'Family' : application.Family ,
                    'Fathersincome' : application.Fathersincome ,
                    'Mothersincome' : application.Mothersincome ,
                    'Approvalstatus' : application.Approvalstatus
                    }
                }, 200
            else:
                return {
                    "error": f"application with ID {application_id} not found"
                }, 404
        except Exception as e:
            db.session.rollback()
            return {
                "message": "Failed to update the application",
                 "error": str(e)
            }, 500
        
