from flask import request, current_app
from functools import wraps
# from server.main import hoge

def fuga_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # global hoge
        print('fuga_check', current_app.config['hoge'])
        current_app.config['hoge'] += 1
        # ここで 認証処理 (...まだ書いていない)
        return func(*args, **kwargs)
    return wrapper