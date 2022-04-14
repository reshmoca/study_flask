from flask import Blueprint, g, current_app
# from controller import user_controller
from logging import config
from json import load
# import auth
import logger
import check

# Generate Router Instance
router = Blueprint('router', __name__)

# Read Logging Configuration
with open("./config/logging.json", "r", encoding="utf-8") as f:
  config.dictConfig(load(f))

@router.route("/", methods=['GET'])
@logger.http_request_logging
@check.fuga_check
# @auth.requires_auth
def hello_world():
    print(type(current_app.config['hoge']))
    print(current_app.config['hoge'])
    print(type(current_app.config['fuga']))
    print(current_app.config['fuga'])
    current_app.config['fuga'] = None
    current_app.logger.info('hello_world {0}'.format(current_app.config['hoge']))
    return "Hello World!! {0}".format(current_app.config['hoge'])

# @router.route("/api/v1/users/getUserList", methods=['GET'])
# @logger.http_request_logging
# @fuga_check
# # @auth.requires_auth
# def api_v1_users_get_user_list():
#     return user_controller.get_user()

@router.after_request
def after_request(response):
  # response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response