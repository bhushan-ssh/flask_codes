from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required



db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    fs_token_uniquifier = db.Column(db.String(255), unique=True, nullable=True)
    roles = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)   


app = Flask(__name__)

app.config['SECRET_KEY'] = 'super-secret'   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///security.db'
app.config['SECURITY_PASSWORD_SALT'] = 'some_salt'

db.init_app(app)



def create_database():
    with app.app_context():
        db.create_all()

        user_role = user_datastore.find_or_create_role(name='user', description='User Role')
        admin_role = user_datastore.find_or_create_role(name='admin', description='Admin Role') 
        manager_role = user_datastore.find_or_create_role(name='manager', description='Manager Role')

        
        if not user_datastore.find_user(username='admin'):
                 user_datastore.create_user(
                    username='admin',
                    email='admin@example.com',
                    password='admin123',
                    roles=[admin_role])


        if not user_datastore.find_user(username='super'):
            user_datastore.create_user(
            username='super',
            email='super@example.com',
            password='super123',
            roles=[manager_role, admin_role])
        

        db.session.commit()
        print("Database and default users created.")











user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)



if __name__ == '__main__':
    create_database()
    app.run(debug=True) 

































































app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)