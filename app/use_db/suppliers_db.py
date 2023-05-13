from app.use_db.tools import quarry


def all_suppliers():
    suppliers = quarry.call("select * from provider", commit=False, fetchall=True)

    return suppliers


def inf_provide(id_p):

    inf_pr = quarry.call("select provider.name_p from provider "
                         "where provider.id_p = %s", [id_p], commit=False, fetchall=False)

    id_adr = quarry.call("select provider.id_adr from provider "
                         "where provider.id_p = %s", [id_p], commit=False, fetchall=False)

    inf_adr = quarry.call("select * from address "
                          "where address.id_adr = %s", [id_adr[0]], commit=False, fetchall=False)

    inf_category = quarry.call("select * from categories "
                               "where categories.id_p = %s", [id_p], commit=False, fetchall=True)

    return inf_adr, inf_category, inf_pr


def all_product(id_cat):

    products = quarry.call("select * from product "
                           "where product.id_cat = %s", [id_cat], commit=False, fetchall=True)

    return products
