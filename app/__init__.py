from flask import Flask

def create_app():
    app = Flask(__name__)

    '''
    # Configure app for secure cookies
    app.config['SESSION_COOKIE_SECURE'] = True  # Only send cookies over HTTPS
    app.config['REMEMBER_COOKIE_SECURE'] = True  # Only send remember me cookies over HTTPS
    app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to session cookies
    '''
    
    from .routes import main
    app.register_blueprint(main)
    return app