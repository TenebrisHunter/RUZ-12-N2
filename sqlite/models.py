from peewee import *

db = SqliteDatabase('data.sqlite3')

class Allteach(Model):
    id = PrimaryKeyField(unique=True)
    label = CharField()
    description = CharField()
    type = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'allteaches'