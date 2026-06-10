import os
from flask import Flask
from app.models import db

def create_app(test_config=None):
    """
    Application Factory to create and configure the Flask app.
    """
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    if test_config is None:
        app.config.from_object('config.Config')
        
        # Override configuration for SQLite database path dynamically
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists for SQLite
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions (called after app.config configuration is set up)
    db.init_app(app)

    # Ensure the parent directory for the SQLite database exists
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI')
    if db_uri and db_uri.startswith('sqlite:///'):
        # Extract file path after 'sqlite:///'
        db_path = db_uri[9:]
        # For sqlite:////path (absolute Linux path), keep the leading slash
        db_dir = os.path.dirname(db_path)
        if db_dir:
            try:
                os.makedirs(db_dir, exist_ok=True)
            except Exception as e:
                app.logger.warning(f"Failed to create database directory {db_dir}: {e}")

    # Automatically create database tables at runtime if they do not exist
    with app.app_context():
        db.create_all()

    # Register blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    @app.route('/health')
    def health():
        return {'status': 'healthy'}, 200

    return app
