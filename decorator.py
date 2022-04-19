from flask import request, current_app, make_response, jsonify
from functools import wraps
import global_var
# from server.main import hoge

def fuga_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('fuga_check', current_app.config)
        print('fuga_check global ', global_var.g_int, global_var.g_obj, global_var.g_array, global_var.g_str)
        global_var.g_int += 1
        global_var.g_obj['check'] = 'fuga_check'
        global_var.g_array.append('fuga_check')
        global_var.g_str = 'fuga_check'
        # ここで 認証処理 (...まだ書いていない)
        return func(*args, **kwargs)
    return wrapper

def fuga_check2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # global hoge
        global_var.g_int += 1
        if global_var.g_int > 5:
            return make_response(jsonify({"message": "g_int > 5"}), 401)
        return func(*args, **kwargs)
    return wrapper
