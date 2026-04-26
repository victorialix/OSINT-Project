from flask import Flask, render_template
from routes.travel_routes import travel_bp
from routes.chart_routes import chart_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(travel_bp, url_prefix="/api")
app.register_blueprint(chart_bp, url_prefix="/api")

# Home page
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
