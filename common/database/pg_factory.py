from contextlib import contextmanager

from common import logger_factory
from common.config import general_config
from common.database.pgbase import PostgresAccessorBase
from sqlalchemy.engine import create_engine


logger = logger_factory.create_logger(__name__)

@contextmanager
def create_scope(model_type=None, database_url=general_config.get_database_url()):
    session = PostgresAccessorBase(model_type=model_type, database_url=database_url)
    try:
        isinstance(session, PostgresAccessorBase)
        yield session
        session.commit()
    except Exception, e:
        logger.error(e)
        session.rollback()
        raise e
    finally:
        session.close()
        session = None


def model_checkable(func):
    def wrapper(**kwargs):
        if 'model_type' in kwargs:
            model_type = kwargs['model_type']
            model_type()
            logger.info(model_type.__name__ + ' is instantiable')
        return func(**kwargs)
    return wrapper

def persistent_checkable(func):
    def wrapper(**kwargs):
        if 'model_type' in kwargs:
            model_type = kwargs['model_type']
            database_url =   general_config.get_database_url()
            if 'database_url' in kwargs:
                database_url = kwargs['database_url']
            if general_config.is_dev():
                connect_args = {'check_same_thread':False}
                engine = create_engine(database_url, echo=False, connect_args=connect_args)
            else:
                engine = create_engine(database_url, echo=False)
            model_type.metadata.create_all(engine)
            logger.info(model_type.__name__ + ' is persistent')
            with  create_scope(model_type=model_type) as session:
                session.query(model_type).first()
            logger.info(model_type.__name__ + ' is accessible')
            engine.dispose()
        return func(**kwargs)
    return wrapper

@model_checkable
@persistent_checkable
def scope_factory(**kwargs):
    """
    this will create merely an accessor
    :param kwargs:
    :return:
    """
    model_type = kwargs['model_type']
    with create_scope(model_type=model_type) as session:
        session.query(model_type).first()
    @contextmanager
    def wrapper():
        """
        Parameters
        +++++++++++++++++++++++++++++
        model_type : the class type
        :rtype :PostgresAccessorBase
        :return:
        """
        model_type = kwargs['model_type']
        with create_scope(model_type=model_type) as scope:
            yield scope
            scope.commit()
    return wrapper

@model_checkable
@persistent_checkable
def unique_scope_factory(**kwargs):
    """
    this will find data based on id or attr_name for once

    Parameters
    =================================
    create_if_none': if True then create a missing object is neccessary
    attr_name (Opsional) : attribute that is going to be used as the search key

    :return:
    """
    model_type = kwargs['model_type']
    attrib_name = 'id'
    if 'attr_name' in kwargs:
        attrib_name = kwargs['attr_name']
    with create_scope(model_type=model_type) as session:
        session.query(model_type).filter(model_type.__dict__[attrib_name] == None).first()
        logger.info(model_type.__name__ + ' is accessible with key ' + attrib_name)
    @contextmanager
    def wrapper(create_if_none=True, **kwargs):
        id=kwargs[attrib_name]
        create_if_none = True
        with create_scope(model_type=model_type) as session:
            entity = session.query(model_type).filter(model_type.__dict__[attrib_name] == id).first()
            if create_if_none and not entity:
                entity = model_type()
                entity.__dict__[attrib_name] = id
                session.add(entity)
                session.commit()
            yield entity
    return wrapper

@model_checkable
@persistent_checkable
def insert_scope_factory(**kwargs):
    """
    this will always create an object as soon as it is called
    :param kwargs: model_type
    :return:
    """
    model_type = kwargs['model_type']
    @contextmanager
    def wrapper(**kwargs):
        with create_scope(model_type=model_type)  as session:
                entity = model_type()
                session.add(entity)
                session.commit()
                yield entity
                session.commit()
    return wrapper


