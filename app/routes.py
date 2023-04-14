from app import app, jsonify, request, Blueprint
from categories.categories import categories


@app.route('/admin_panel/api/v1.0/')
def index():
    return jsonify("hello world")


app.register_blueprint(categories, url_prefix='/admin_panel/api/v1.0/')
