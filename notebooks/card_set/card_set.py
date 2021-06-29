from ygoprodeck import *

from notebooks import db

ygo = YGOPro()

def card_set_insert(rel):
    query = """insert into card_set values(%s, %s, %s, %s, %s) on conflict (card_cod, set_cod, rarity) do nothing;"""
    data = (rel['card_cod'], rel['set_code'][:3], rel['set_rarity'], rel['set_rarity_code'], float(rel['set_price']))
    db.make_query(query, data)


if __name__ == '__main__':
    # add_cards_from_set('Legend of Blue Eyes White Dragon')
    d = ygo.get_cards(cardset='Legend of Blue Eyes White Dragon')['data']
    for i in d[0]:
        print(i, d[0][i])
