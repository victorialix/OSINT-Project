from flask import Flask
from routes.travel_routes import travel_bp
from routes.chart_routes import chart_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(travel_bp, url_prefix="/api")
    app.register_blueprint(chart_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
