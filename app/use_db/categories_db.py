from app.use_db.tools import quarry


def create_categories(id_p, name_category):
    quarry.call("insert into categories (id_p, name_cat) "
                "values (%s, %s)", [id_p, name_category], commit=True, fetchall=False)


def all_categories(id_p):
    categories = quarry.call("select id_cat, name_cat from categories where id_p = %s",
                             [id_p], commit=False, fetchall=True)

    return categories


def delete_category(id_cat):
    quarry.call("delete from categories where id_cat = %s", [id_cat],
                commit=True, fetchall=False)


def get_category_with_product(id_cat):
    products = quarry.call("select * from product where id_cat = %s", [id_cat],
                           commit=False, fetchall=True)

    name_cat = quarry.call("select name_cat from categories where id_cat = %s", [id_cat],
                           commit=False, fetchall=False)

    return name_cat, products
