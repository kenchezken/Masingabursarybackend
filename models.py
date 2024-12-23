from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    Nationalid = db.Column(db.String)
    Phonenumber = db.Column(db.String)
    Role = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class TertiaryApplication (db.Model):
    __tablename__ = 'tertiaryapplication'

    id = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String) 
    Middlename = db.Column(db.String)
    Lastname = db.Column(db.String)
    Gender = db.Column(db.String)
    Phonenumber = db.Column(db.String)
    Nationalid = db.Column(db.String)
    GuardiansNo = db.Column(db.String)
    Guardianid = db.Column(db.String)
    Disability = db.Column(db.String)
    Ward = db.Column(db.String)
    Location = db.Column(db.String)
    Sublocation = db.Column(db.String)
    Village = db.Column(db.String)
    Chiefname =db.Column(db.String)
    Chiefphonenumber = db.Column(db.Integer)
    AssistantChiefname =db.Column(db.String)
    Assistantchiefno = db.Column(db.String)
    Instituition = db.Column(db.String)
    University = db.Column(db.String)
    Amountexpecting = db.Column(db.String)
    Amountreceived = db.Column(db.String)
    Admno = db.Column(db.String)
    levelofstudy = db.Column(db.String)
    Modeofstudy = db.Column(db.String)
    Yearofstudy = db.Column(db.String)
    Semester = db.Column(db.String)
    Coarseduration = db.Column(db.String)
    Family = db.Column(db.String)
    Fathersincome = db.Column(db.String)
    Mothersincome = db.Column(db.String)
    Imageurl = db.Column(db.String)
    Approvalstatus = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())