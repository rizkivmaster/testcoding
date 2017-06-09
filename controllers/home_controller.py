from flask import render_template, request, redirect
from flask.blueprints import Blueprint

from accessors import shopee_user
from common import logger_factory, bay_time
from common.config import general_config
from common.database.pg_factory import scope_factory

home_router = Blueprint(__name__, __name__)

running_date = bay_time.now()

logger = logger_factory.create_logger(__name__)

user_scope = scope_factory(model_type=shopee_user.User)
@home_router.route('user_register', methods=['GET', 'POST'])
def user_register():
    try:
        error = None
        if request.method == 'POST':
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            with user_scope() as scope:
                    user = shopee_user.User()
                    user.email = email
                    user.username = username
                    user.password = password
                    scope.add(user)
            return redirect('..')
        return render_template('user_register.html', data={'host_url': general_config.get_host_url()}, error=error)
    except Exception as e:
        logger.error(e)

@home_router.route('seller_register')
def seller_register():
    try:
        return render_template('seller_register.html', data={'host_url': general_config.get_host_url()})
    except Exception as e:
        logger.error(e)

@home_router.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with user_scope() as scope:
            existing_user = scope.query(shopee_user.User).filter(shopee_user.User.username == username).first()
            if existing_user is None:
                error = 'User is not found. You can register <a href=\"http://127.0.0.1:29000/user_register\">here.</a>'
            else:
                if existing_user.password == password:
                    return redirect('seller_register')
                else:
                    error = 'Wrong password'
    return render_template('index.html', data={'host_url': general_config.get_host_url()}, error=error)
