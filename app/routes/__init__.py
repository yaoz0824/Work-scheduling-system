from app.routes.main import main_bp
from app.routes.record import record_bp
from app.routes.setting import setting_bp

def register_blueprints(app):
    """註冊所有的 Flask Blueprints"""
    app.register_blueprint(main_bp)
    app.register_blueprint(record_bp)
    app.register_blueprint(setting_bp)
