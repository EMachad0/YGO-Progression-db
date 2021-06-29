import json

import ygoprodeck

from notebooks import sets, cards, card_set

ygo = ygoprodeck.YGOPro()

ALL_SETS = "all_sets.json"

sets_to_insert = {
    'Legend of Blue Eyes White Dragon'
}

def set_full_insert(sett):
    sets.set_insert(sett)
    crd = ygo.get_cards(cardset=sett['set_name'])['data']
    for card in crd:
        cards.card_insert(card)
        for rel in card['card_sets']:
            if sett['set_name'] == rel['set_name']:
                rel['card_cod'] = card['id']
                card_set.card_set_insert(rel)
                

if __name__ == '__main__':
    f = open(ALL_SETS, "r")
    j = json.loads(f.read())
    for s in j:
        if s['set_name'] in sets_to_insert:
            set_full_insert(s)
