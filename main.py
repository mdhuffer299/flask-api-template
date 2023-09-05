def default_app(*args, **kwargs):
    from flask import Flask
    app = Flask(__name__)
    return app.wsgi_app(*args, **kwargs)

def rest_app(*args, **kwargs):
    from config import DevelopmentConfig
    import controllers.rest
    rest = controllers.rest.create_rest_app(DevelopmentConfig)
    return rest.wsgi_app(*args, **kwargs)
