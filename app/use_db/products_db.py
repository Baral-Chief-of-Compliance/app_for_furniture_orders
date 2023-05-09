from app.use_db.tools import quarry


def create_product(atr):
    quarry.call("insert into product(id_cat, name_product, quantity_product, "
                "price_product, description_product, color_product, "
                "height_product, width_product, long_product) values "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s)", atr, commit=True,
                fetchall=False
                )
