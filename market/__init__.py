
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os


os.environ['FLASK_APP'] = 'market'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_market.db'

db = SQLAlchemy(app)

def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_222URI'] = 'sqlite:///new_market.db'
    # your app configuration and routes
    db.init_app(app)
    
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app


# from app import app, db, item
# with app.app_context():
#     data = item.query.all()
    
#     for item in data:

#     item1 = item(name='Test Item', price=100, barcode='123456789', description='Test Description')
#     db.session.add(item1)
#     db.session.commit()
#     items = item.query.all()
#     print(items)
 


 




# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>Welcome to the about page of {username}</h1>'











# import os
# os.environ['FLASK_ENV'] = 'development'
# os.environ['FLASK_DEBUG'] = '1'