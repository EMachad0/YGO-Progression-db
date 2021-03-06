import json

import ygoprodeck

from notebooks import sets, cards, pull

ygo = ygoprodeck.YGOPro()

ALL_SETS = "all_sets.json"

sets_to_insert = {
    'Legend of Blue Eyes White Dragon',
    'Metal Raiders',
    'Magic Ruler',
    "Pharaoh's Servant",
    'Labyrinth of Nightmare'
}

def set_full_insert(sett):
    sets.set_insert(sett)
    crd = ygo.get_cards(cardset=sett['set_name'])['data']
    for card in crd:
        card["desc"] = card["desc"].replace('"', '&#34;').replace("'", '&#33;')
        cards.card_insert(card)
        for rel in card['card_sets']:
            if sett['set_name'] == rel['set_name']:
                rel['card_cod'] = card['id']
                pull.card_set_insert(rel)
        print(card['name'])
                

if __name__ == '__main__':
    f = open(ALL_SETS, "r")
    j = json.loads(f.read())
    for s in j:
        if s['set_name'] in sets_to_insert:
            set_full_insert(s)
