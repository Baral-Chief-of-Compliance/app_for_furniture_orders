from app import Blueprint, jsonify, request
from app.use_db import categories_db


categories = Blueprint('categories', __name__)


@categories.route('/categories', methods=['GET', 'POST'])
def all_categories():
    if request.method == 'POST':
        id_p = request.json["id_p"]
        categories_name = request.json["categories_name"].lower()

        categories_db.create_categories(id_p, categories_name)

        return jsonify(f"category {categories_name} for provide {id_p} is add")

    elif request.method == "GET":

        json_categories = []

        categories = categories_db.all_categories(1)

        for cat in categories:
            json_categories.append({"id_cat": cat[0], "name_cat": cat[1]})

        return jsonify(json_categories)


@categories.route('/categories/<int:id_cat>', methods=['GET', 'POST', 'DELETE'])
def show_categories_for_employer(id_cat):
    if request.method == "DELETE":
        categories_db.delete_category(id_cat)

        return jsonify(f"category {id_cat} is delete")

    elif request.method == "GET":
        json_products = []

        name_cat, products = categories_db.get_category_with_product(id_cat)

        for product in products:
            json_products.append({
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

        inf_category = {
            "name": name_cat[0],
            "products": products
        }

        return jsonify(inf_category)

