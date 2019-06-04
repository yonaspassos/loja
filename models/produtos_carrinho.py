import peewee

from models.carrinho import Cart
from models.produto import Product
from settings import db_host, db_password, db_port, db_user

db = peewee.PostgresqlDatabase('loja', user=db_user, password=db_password, host=db_host, port=db_port)

class Product_cart(peewee.Model):
    cart_id = peewee.ForeignKeyField(Cart)
    product_id = peewee.ForeignKeyField(Product)

    class Meta:
        database = db