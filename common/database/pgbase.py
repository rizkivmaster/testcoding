from common.config import general_config
from sqlalchemy.pool import NullPool

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlalchemy import BigInteger
from sqlalchemy.dialects import postgresql, mysql, sqlite

BigIntegerType = BigInteger()
BigIntegerType = BigIntegerType.with_variant(postgresql.BIGINT(), 'postgresql')
BigIntegerType = BigIntegerType.with_variant(mysql.BIGINT(), 'mysql')
BigIntegerType = BigIntegerType.with_variant(sqlite.INTEGER(), 'sqlite')

class PostgresAccessorBase(Session):
    def __init__(self, model_type, database_url):
        self.model_base = model_type
        if general_config.is_dev():
            connect_args = {'check_same_thread':False}
            engine = create_engine(database_url, echo=False, connect_args=connect_args, poolclass=NullPool)
        else:
            engine = create_engine(database_url, echo=False, poolclass=NullPool)
        super(PostgresAccessorBase, self).__init__(bind=engine)



