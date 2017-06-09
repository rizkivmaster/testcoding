from common import bay_time
from common.database import modelbase
from common.database.pgbase import BigIntegerType
from sqlalchemy import Column, Integer, String, DateTime


class User(modelbase.ModelBase):
    __tablename__ = 'shopee_users'
    id = Column(BigIntegerType, primary_key=True, autoincrement=True)
    username = Column(String, index=True)
    password = Column(String)
    email = Column(String)

    def __init__(self):
        self.username = None
        self.password = None
        self.email = None