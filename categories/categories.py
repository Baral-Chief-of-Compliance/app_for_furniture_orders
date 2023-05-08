from app import Blueprint, jsonify, request
from app.use_db import categories_db


categories = Blueprint('categories', __name__)


@categories.route('/categories', methods=['GET', 'POST'])
def all_categories():
    if request.method == 'POST':
        json_characteristics = []
        name_category = request.json["name_category"]
        characteristics = request.json["characteristics"]
        print(name_category, characteristics)

        for c in characteristics:
            json_characteristics.append(c["value"])

        json_characteristics.append('цена')
        json_characteristics.append('количество')
        json_characteristics.append('описание')
        json_characteristics.append('рейтинг')
        json_characteristics.append('id_p')

        print({
            "name_category": name_category,
            "characteristics": json_characteristics
        })

        categories_db.create_categories(name_category, json_characteristics, 1)
        return jsonify({
            "name_category": name_category,
            "characteristics": json_characteristics
        })


@categories.route('/categories/<int:id>', methods=['GET', 'POST'])
def show_categories_for_employer(id):
    if request.method == 'GET':
        categories = []
        all_tables = categories_db.show_tables_for_operator()

        for t in all_tables:
            print(t[0])
            if "_" in t[0]:
                print("нашел")
                new_t = t[0].split("_")
                print(new_t[0])
                if new_t[1] == f'{id}':
                    categories.append({
                        "name": new_t[0]
                    })

        return jsonify({
            "categories": categories
        })
