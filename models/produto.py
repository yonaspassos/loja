import peewee
from settings import db_host, db_password, db_port, db_user

db = peewee.PostgresqlDatabase('loja', user=db_user, password=db_password, host=db_host, port=db_port)

class Product(peewee.Model):
    name = peewee.CharField()
    price = peewee.DecimalField()

    class Meta:
        database = db