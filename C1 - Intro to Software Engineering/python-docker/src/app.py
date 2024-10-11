from flask import Flask
from livereload import Server
from routes import register_routes  # Import routes from a separate file

def create_app():
    app = Flask(__name__)

    # Configure app (you can load configuration from files or environment)
    app.config.from_object('config.Config')

    # Register routes
    register_routes(app)  # Use a function to keep routes organized

    # Any other setup (e.g., registering extensions)

    return app

if __name__ == '__main__':
    app = create_app()
    server = Server(app.wsgi_app)
    server.watch('functions.py')  # Watch for Python file changes
    server.watch('templates/*.html')  # Watch for changes in HTML templates
    server.serve(host='0.0.0.0', port=8000, liveport="3000", debug=True)