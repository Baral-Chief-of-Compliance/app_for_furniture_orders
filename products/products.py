from app import Blueprint, jsonify, request
from app.use_db import products_db


products = Blueprint('products', __name__)


@products.route('/products', methods=['POST'])
def create_product():
    if request.method == "POST":
        id_cat = request.json["id_cat"]
        name_product = request.json["name_product"]
        quantity_product = request.json["quantity_product"]
        price_product = request.json["price_product"]
        description_product = request.json["description_product"]
        color_product = request.json["color_product"]
        height_product = request.json["height_product"]
        width_product = request.json["width_product"]
        long_product = request.json["long_product"]

        atr = [id_cat, name_product, quantity_product,
               price_product, description_product, color_product,
               height_product, width_product, long_product]

        products_db.create_product(atr)

        return jsonify(f"product {name_product} for {id_cat} is add")
