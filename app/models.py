from app import db
from peewee import *


class BaseModel(Model):
    class Meta:
        database = db.database


class DbModel(BaseModel):
    col1 = PrimaryKeyField(null=False)
    col2 = IntegerField()
    col3 = CharField(3)

    @property
    def serialize(self):
        data = {
            'col1': str(self.col1).strip(),
            'col2': str(self.col2).strip(),
            'col3': str(self.col3).strip()
        }

        return data

    def __repr__(self):
        return f"{self.col1, self.col2, self.col3}"
