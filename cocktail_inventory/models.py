from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow 

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = True, default = '')
    username = db.Column(db.String(150), nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
   # cocktail = db.relationship('Cocktail', backref = 'owner', lazy =True)
    
    
    def __init__(self, email, username, first_name = '', last_name = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username
        self.token = self.set_token(24)
        

    def set_token(self, length):
        return secrets.token_hex(length)
        
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} has been added to the database!"
    


class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    instructions = db.Column(db.String(800),nullable =True)
    img = db.Column(db.String(800))
    ingredient1 = db.Column(db.String(800),nullable = True)
    ingredient2 = db.Column(db.String(800),nullable = True)
    ingredient3= db.Column(db.String(800),nullable = True)
    ingredient4 = db.Column(db.String(800),nullable = True)
    ingredient5= db.Column(db.String(800),nullable = True)
    ingredient6= db.Column(db.String(800),nullable = True)
    ingredient7= db.Column(db.String(800),nullable = True)
    ingredient8= db.Column(db.String(800),nullable = True)
    ingredient9= db.Column(db.String(800),nullable = True)
    ingredient10= db.Column(db.String(800),nullable = True)
    ingredient11= db.Column(db.String(800),nullable = True)
    ingredient12= db.Column(db.String(800),nullable = True)
    ingredient13= db.Column(db.String(800),nullable = True)
    ingredient14= db.Column(db.String(800),nullable = True)
    ingredient15= db.Column(db.String(800),nullable = True)
    measure1= db.Column(db.String(800),nullable =True)
    measure2= db.Column(db.String(800),nullable =True)
    measure3= db.Column(db.String(800),nullable =True)
    measure4= db.Column(db.String(800),nullable =True)
    measure5= db.Column(db.String(800),nullable =True)
    measure6= db.Column(db.String(800),nullable =True)
    measure7= db.Column(db.String(800),nullable =True)
    measure8= db.Column(db.String(800),nullable =True)
    measure9= db.Column(db.String(800),nullable =True)
    measure10= db.Column(db.String(800),nullable =True)
    measure11= db.Column(db.String(800),nullable =True)
    measure12= db.Column(db.String(800),nullable =True)
    measure13= db.Column(db.String(800),nullable =True)
    measure14= db.Column(db.String(800),nullable =True)
    measure15= db.Column(db.String(800),nullable =True)


    def __init__(self,id,name,img):
        self.id =id
        self.name=name
        self.img=img



    def to_dict(self, dict):
        self.id=dict['id']
        self.name = dict['name']
        self.img =dict['img']
        self.instructions =dict['instructions']
        self.ingredient1 = dict['ingredient1']
        self.ingredient2 = dict['ingredient2']
        self.ingredient3 =dict['ingredient3']
        self.ingredient4 =dict['ingredient4']
        self.ingredient5 =dict['ingredient5']
        self.ingredient6 =dict['ingredient6']
        self.ingredient7 =dict['ingredient7']
        self.ingredient8 =dict['ingredient8']
        self.ingredient9 =dict['ingredient9']
        self.ingredient10 =dict['ingredient10']
        self.ingredient11 =dict['ingredient11']
        self.ingredient12 =dict['ingredient12']
        self.ingredient13 =dict['ingredient13']
        self.ingredient14 =dict['ingredient14']
        self.ingredient15 =dict['ingredient15']
        self.measure1 =dict['measure1']
        self.measure2 =dict['measure2']
        self.measure3 =dict['measure3']
        self.measure4 =dict['measure4']
        self.measure5 =dict['measure5']
        self.measure6 =dict['measure6']
        self.measure7 =dict['measure7']
        self.measure8 =dict['measure8']
        self.measure9 =dict['measure9']
        self.measure10 =dict['measure10']
        self.measure11 =dict['measure11']
        self.measure13 =dict['measure13']
        self.measure14 =dict['measure14']
        self.measure15 =dict['measure15']
        


    

    def __repr__(self):
        return f"Cocktail {self.name} has been added to the database!"
    
    def saved(self):
        db.session.add(self)
        db.session.commit

    def known_cocktail(id):
        return Cocktail.query.get(id)
    

class CocktailSchema(ma.Schema): 
    class Meta:
        fields = ['id', 'name', 'instructions', 'img', 'ingredient1', 'ingredient2','ingredient3','ingredient4', 'ingredient5','ingredient6', 'ingredient7', 'ingredient8', 'ingredient9', 'ingredient10',
                  'ingredient11', 'ingredient12', 'ingredient13','ingredient14','ingredient15', 'measure1', 'measure2', 'measure3', 'measure4', 'measure5', 'measure6', 'measure7', 'measure8', 'measure9',
                  'measure10','measure11', 'measure12','measure13', 'measure14', 'measure15']

cocktail_schema = CocktailSchema()
cocktails_schema = CocktailSchema(many = True)





 





 
        
