import json

banlist = {}
key = 3
while True:
    try:
        card = input().replace('\r', "").replace('"', '&#34;').replace("'", '&#33;')
        if "Monster Cards" in card or "Magic Cards" in card or "Trap Cards" in card:
            continue
        if card == "Forbidden":
            key = 0
        elif card == "Limited":
            key = 1
        elif card == "Semi-Limited":
            key = 2
        elif card == "Unlimited":
            key = 3
        elif key == 3:
            continue
        else:
            banlist[card] = key
    except EOFError:
        print(f"'{json.dumps(banlist)}'")
        break