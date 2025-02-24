from flask import Flask
from config import Config
from routes import optimization_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(optimization_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    # app.run(host="0.0.0.0", port=5000, ssl_context=('server.cert', 'server.key'))
    app.run(host="0.0.0.0", port=5000)

