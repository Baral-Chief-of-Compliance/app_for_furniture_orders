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
