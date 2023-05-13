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


@products.route('/products/<int:id_product>', methods=['GET'])
def product(id_product):

    product = products_db.show_inf_about_product(id_product)

    return jsonify({
        "id_product": product[0],
        "name_product": product[2],
        "quantity_product": product[3],
        "price_product": product[4],
        "raiting_product": product[5],
        "description_product": product[6],
        "color_product": product[7],
        "height_product": product[8],
        "width_product": product[9],
        "long_product": product[10]
    })
