import json
from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound,BadRequest,InternalServerError
import datetime

error_bp = Blueprint('error', __name__)

def res(val):
    return jsonify({ 
        "error": val, 
        "time": datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
    })

@error_bp.app_errorhandler(BadRequest)
def error_handler(e):
    print('BadRequest', type(e), e)
    return res('BadRequest'), 500

@error_bp.app_errorhandler(NotFound)
def error_handler(e):
    print('NotFound', type(e), e)
    return res('NotFound'), 500

@error_bp.app_errorhandler(InternalServerError)
def error_handler(e):
    print('InternalServerError', type(e), e)
    return res('InternalServerError'), 500

@error_bp.app_errorhandler(ValueError)
def error_handler(e):
    print('ValueError', type(e), e)
    return res('ValueError'), 500

@error_bp.app_errorhandler(Exception)
def error_handler(e):
    print('Exception', type(e), e)
    return res('Exception'), 500
