from app import Blueprint, jsonify, request
from app.use_db import suppliers_db


suppliers = Blueprint('suppliers', __name__)


@suppliers.route('/suppliers', methods=['GET'])
def all_suppliers():
    if request.method == "GET":
        json_suppliers = []
        suppliers = suppliers_db.all_suppliers()

        for sup in suppliers:
            json_suppliers.append({
                "id_p": sup[0],
                "name_p": sup[1]
            })

        return jsonify(json_suppliers)


@suppliers.route('/suppliers/<int:id_p>', methods=['GET'])
def inf_provider(id_p):
    if request.method == 'GET':
        json_categories = []

        inf_adr, inf_category, inf_pr = suppliers_db.inf_provide(id_p)

        for cat in inf_category:
            products = suppliers_db.all_product(cat[0])

            cat_dict = {
                "id_cat": cat[0],
                "name_cat": cat[2],
                "products": []
            }

            for product in products:
                cat_dict["products"].append({
                    "id_product": product[0],
                    "name_product": product[2],
                    "quantity_product": product[3],
                    "price_product": product[4]
                })

            json_categories.append(cat_dict)

        return jsonify({
            "name_p": inf_pr[0],
            "town": inf_adr[1],
            "street_adr": inf_adr[2],
            "house_adr": inf_adr[3],
            "frame_adr": inf_adr[4],
            "longitude_adr": inf_adr[5],
            "latitude_adr": inf_adr[6],
            "index_addr": inf_adr[7],
            "categories": json_categories
        })




