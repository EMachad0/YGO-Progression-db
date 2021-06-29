from notebooks import db

def set_insert(sett):
    query = """insert into set values(%s, %s, %s, %s) on conflict (set_cod) do nothing;"""
    data = (sett['set_code'], sett['set_name'], sett['num_of_cards'], sett['tcg_date'])
    db.make_query(query, data)

    