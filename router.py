from flask import Blueprint, g, current_app, abort
# from controller import user_controller
from logging import config
from json import load
# import auth
import logger
import decorator
import global_var
from werkzeug.exceptions import NotFound,BadRequest,InternalServerError


# Generate Router Instance
router = Blueprint('router', __name__)

# Read Logging Configuration
# with open("./config/logging.json", "r", encoding="utf-8") as f:
#   config.dictConfig(load(f))

@router.route("/", methods=['GET'])
@logger.http_request_logging
@decorator.fuga_check
# @auth.requires_auth
def hello_world():
    print(type(current_app.config['hoge']))
    print(current_app.config['hoge'])
    print('hello_world global ', global_var.g_int, global_var.g_obj, global_var.g_array, global_var.g_str)
    global_var.g_int += 1
    global_var.g_obj['router'] = 'hello_world'
    global_var.g_array.append('hello_world')
    global_var.g_str = 'hello_world'
    current_app.config['fuga'] = None
    current_app.logger.info('hello_world {0}'.format(current_app.config['hoge']))
    return "Hello World!! {0}".format(current_app.config['hoge'])


@router.route("/error1", methods=['GET'])
def error1():
  print('error1')
  abort(404)

@router.route('/error2')
def error2():
  print('error2')
  raise NotFound

@router.route('/error3')
def error3():
  print('error3')
  raise ValueError('hogehoge value error')

@router.route('/error4')
def error4():
  print('error4')
  raise Exception('hogehoge Exception')

# @router.route("/api/v1/users/getUserList", methods=['GET'])
# @logger.http_request_logging
# @fuga_check
# # @auth.requires_auth
# def api_v1_users_get_user_list():
#     return user_controller.get_user()
@router.before_request
def before_request(response):
  print('before_request')
  print('before_request global ', global_var.g_int, global_var.g_obj, global_var.g_array, global_var.g_str)
  global_var.g_int += 1
  global_var.g_obj['router'] = 'before_request'
  global_var.g_array.append('before_request')
  global_var.g_str = 'before_request'
  return response

@router.after_request
@decorator.fuga_check2
def after_request(response):
  print('after_request')
  print('after_request global ', global_var.g_int, global_var.g_obj, global_var.g_array, global_var.g_str)
  global_var.g_int += 1
  global_var.g_obj['router'] = 'after_request'
  global_var.g_array.append('after_request')
  global_var.g_str = 'after_request'
  # response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response