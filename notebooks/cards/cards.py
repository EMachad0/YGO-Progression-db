from ygoprodeck import *

from notebooks import db

ygo = YGOPro()

link_val = {'Top':1, 'Top-Left':2, 'Left':4, 'Bottom-Left':8, 'Bottom':16, 'Bottom-Right':32, 'Right':64, 'Top-Right':128}
def link_to_mask(arr):
    if arr is None:
        return None
    my_val = 0
    for a in arr:
        my_val += link_val[a]
    return my_val

def card_insert(c):
    query = """insert into card values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) on conflict (card_cod) do nothing;"""
    data = (c['id'], c['name'], c['type'], c['desc'],
            c.get('atk'), c.get('def'), c.get('level'), c.get('scale'),
            c.get('race'), c.get('attribute'), c.get('archetype'), c.get('card_images')[0]['id'],
            c.get('linkval'), link_to_mask(c.get('linkmarkers')))
    db.make_query(query, data)
        

if __name__ == '__main__':
    # add_cards_from_set('Legend of Blue Eyes White Dragon')
    d = ygo.get_cards(cardset='Legend of Blue Eyes White Dragon')['data']
    for i in d[0]:
        print(i, d[0][i])
