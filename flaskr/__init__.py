import os

from flask import Flask


def create_app(test_config=None):
    # creamos y configuramos la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Cargue la configuración de la instancia, si existe, cuando no se esté probando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Cargue la configuración de prueba si se pasa en
        app.config.from_mapping(test_config)

    # Asegúrese de que exista la carpeta de instancia
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Una página sencilla que dice hola
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app