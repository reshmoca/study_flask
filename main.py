#!/usr/bin/python3
from cmath import log
from flask import Flask
from flask_cors import CORS
import router
import logging
from logging import handlers
# from config import config
# import db
# from logging.config import dictConfig
# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })
def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)

    # Read DB setting & Initialize
    # app.config.from_object(config.Config)
    # db.init_db(app)
    # db.init_ma(app)

    # logger
    # logging.config.dictConfig({
    #     'version': 1,
    #     'formatters': {'default': {
    #         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    #     }},
    #     'handlers': {'wsgi': {
    #         'class': 'logging.StreamHandler',
    #         'stream': 'ext://flask.logging.wsgi_errors_stream',
    #         'formatter': 'default'
    #     }},
    #     'root': {
    #         'level': 'INFO',
    #         'handlers': ['wsgi']
    #     }
    # })

    # see:https://hawksnowlog.blogspot.com/2020/10/flask-logging-architecture.html#%E3%81%A8%E3%82%8A%E3%81%82%E3%81%88%E3%81%9A%E6%A8%99%E6%BA%96%E3%81%AE%E3%83%AD%E3%82%B0%E3%82%92%E7%A2%BA%E8%AA%8D%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B
    # see:https://oboe2uran.hatenablog.com/entry/2020/10/27/210621
    # https://docs.python.org/ja/3/library/logging.handlers.html?highlight=logging%20handler
    log_file_path = 'logs/hoge.txt'
    # app.logger.setLevel(logging.DEBUG)
    # file設定
    log_handler = logging.FileHandler(log_file_path)
    log_handler.setLevel(logging.DEBUG)
    log_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    app.logger.addHandler(log_handler)
    # ローテーション
    log_handler = handlers.TimedRotatingFileHandler(filename=log_file_path,
                                            encoding='UTF-8',
                                            when='s',
                                            backupCount=10)
    app.logger.addHandler(log_handler)

    # Register Router Instance
    app.register_blueprint(router.router)

    # Additional Configuration 
    app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
    app.config["JSON_SORT_KEYS"] = False #ソートをそのまま
    CORS(
        app,
        resources = {
            r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
        }
    )
    app.config['hoge'] = 0
    fuga = {}
    fuga['hoi'] = 'hai'
    app.config['fuga'] = fuga

    print('create_app', app.config['hoge'])
    return app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True, use_reloader=False)
