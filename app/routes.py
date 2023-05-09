from app import app, jsonify, request, Blueprint
from categories.categories import categories
from products.products import products


url = '/admin_panel/api/v1.0/'


@app.route(url)
def index():
    return jsonify("hello world")


app.register_blueprint(categories, url_prefix=url)
app.register_blueprint(products, url_prefix=url)
