#techblog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app=Flask(__name__)

###############DATABASE SETUP###########
app.config['SECRET_KEY']="mysecretkey"
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
app.db=db
Migrate(app,db)
################# Setup COmplete###################

###################LOGIN SETUP #######################
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'
############### SETUP COMPLETE######################

from Thetechblog.core.views import core
from Thetechblog.users.views import users
from Thetechblog.blogposts.views import blogposts
from Thetechblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blogposts)
app.register_blueprint(error_pages)



