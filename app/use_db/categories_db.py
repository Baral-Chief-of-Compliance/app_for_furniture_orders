from app.use_db.tools import quarry


def create_categories(name_category, characteristics, id_p):
    quarry_text = f"create table {name_category}_{id_p} ( id_c int unique auto_increment not null, "
    for c in characteristics:
        if c == "цена":
            quarry_text = quarry_text + f"цена DECIMAL(10, 2), "
        elif c == "количество":
            quarry_text = quarry_text + f"количество int, "
        elif c == "описание":
            quarry_text = quarry_text + f"описание text, "
        elif c == "рейтинг":
            quarry_text = quarry_text + f"рейтинг int, "
        elif c == "id_p":
            quarry_text = quarry_text + f"id_p int, "
        else:
            quarry_text = quarry_text + f"{c} varchar(50), "

    quarry_text = quarry_text + f"primary key (id_c, id_p), "
    quarry_text = quarry_text + f"foreign key (id_p) references provider(id_p) on delete cascade on update cascade );"

    quarry.call(quarry_text, commit=True, fetchall=False)


def show_tables_for_operator():
    inf = quarry.call("select table_name from information_schema.columns where column_name = %s",
                      ['id_p'], commit=False, fetchall=True)

    print(inf)

    return inf