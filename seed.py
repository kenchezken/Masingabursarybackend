from faker import Faker
import random
from app import app
from datetime import datetime

from models import db , User , TertiaryApplication

fake = Faker()

with app.app_context():

    Rolearray = ['Admin' , 'Student']
    BursaryApproved = ['TRUE' , 'FALSE']

    User.query.delete()
    TertiaryApplication.query.delete()

    print("🦸‍♀️ Seeding users...")
    
    users = []

    for i in range(20):
        userobject = User(
            Nationalid =  random.choice(['37892469' , '11111111']) ,
            Phonenumber = fake.random_number() ,
            Role = random.choice(Rolearray),
            password = random.choice(['ken' , 'don']),
        )
        users.append(userobject)
        db.session.add_all(users)
        print(users)
        db.session.commit()
    
    print("🦸‍♀️ seeding application...")

    Applicationarray = []
    for i in range(20):
        Applicationobject = TertiaryApplication(
         Firstname = fake.name() ,
         Middlename = fake.name() ,
         Lastname = fake.name() ,
         Gender = random.choice(['Female' , 'Male']),
         Nationalid = random.choice(['37892469' , '11111111']) ,
         GuardiansNo = fake.name() ,
         Guardianid = fake.name() ,
         Disability = random.choice(['TRUE' , 'FALSE']) ,
         Ward = random.choice(['MASINGACENTRAL', 'EKALAKALAIKATINI' , 'MUTHESYA' , 'NDITHINI']) ,
         Location = random.choice(['Masinga central' , 'EkalakalaIkatini' , 'Muthesya']) ,
         Sublocation = fake.name() ,
         Village = fake.name() ,
         Instituition = fake.name() ,
         Admno = fake.name() ,
         Modeofstudy = fake.name() ,
         Yearofstudy = fake.name() ,
         Semester = fake.name() ,
         Coarseduration = random.choice(['1' , '2' ,'3' , '3'])
        )
  
        Applicationarray.append(Applicationobject)
        db.session.add_all(Applicationarray)
        print(Applicationarray)
        db.session.commit()