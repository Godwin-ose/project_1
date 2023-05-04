from market import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)
 


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
    

def initialize():
    from market import app
    with app.app_context():
        db.create_all()
        
        item2 = Item(name='Samsung s32', price=80000, barcode='7869876545', description='A new item for sale.')
        item3 = Item(name='Samsung galaxy 22', price=100000, barcode='7689987326', description='very good with pictures')
        item4 = Item(name='Apple air', price=354000, barcode='9897641325', description='The latest laptop.')
        item5 = Item(name='LG tv 3ee', price=200000, barcode='5576987433', description='tv with swag.')
        item6 = Item(name='Sony camera tr34', price=134000, barcode='5412357898', description='This camera has the best range ever.')

        db.session.add_all([item2, item3, item4, item5, item6])
        db.session.commit()
        
        
        


