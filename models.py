from config import db

class Product(db.Model):           #   model--->ORM model--class is aware about--db column ans orm mapping--object ko map kiya gya hai relatinal
    id = db.Column('prod_id', db.Integer, primary_key=True)
    name = db.Column('prod_name', db.Sring(30))
    qyt = db.Column('prod_qyt', db.Integer)
    price = db.Column('prod_price', db.float)
    vendor = db.Column('prod_vendor', db.String(30))


