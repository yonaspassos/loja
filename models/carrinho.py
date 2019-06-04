import peewee
from settings import db_host, db_password, db_port, db_user

db = peewee.PostgresqlDatabase('loja', user=db_user, password=db_password, host=db_host, port=db_port)

class Cart(peewee.Model):
    client_name = peewee.CharField()

    class Meta:
        database = db