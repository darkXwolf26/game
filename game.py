import copy
import random
def show_stats():
    print(f"{player['name']} | {player['health']} | {player['attack']} | {player['stats']['strength']} | {player['stats']['dexterity']}")

def show_room():
    print(f"{current_room['name']} | {current_room['description']}")
    for direction, destination in current_room["exits"].items():
        print(f"{direction} >>> {destination}")

        
sword = r'''
   ()
   )(
o======o
   ||
   ||
   ||
   ||
   ||
   ||
   ||
   ||
   ||
   \/'''

player = {
    "name": "Jeff",
    "health": 100,
    "attack": 15,
    "alive": True,
    "gold": 30,
    "inventory": ["sword", "health potion"],
    "stats": {"strength": 8, "dexterity": 6},
    "regen": 0,
    "regen rounds": 0
}

merchant = {
    "health potion": {"name": "health potion", "price": 40, "description": "Heals 30 health instantly."},
    "bandage": {"name": "bandage", "price": 25, "description": "Heals 25 health over time."},
    "enchanted sword": {"name": "enchanted sword", "price": 150, "description": "It is said to make you braver, and is more powerful than a regular sword."},
    "torch": {"name": "torch", "price": 15, "description": "Burns bright."}
}

goblin = {
    "name": "goblin",
    "max health": 30,
    "health": 30,
    "attack": 8,
    "gold": 5
}

troll = {
    "name": "troll",
    "max health": 55,
    "health": 55,
    "attack": 20,
    "gold": 30
}
orc = {
    "name": "orc",
    "max health": 50,
    "health": 50,
    "attack": 15,
    "gold": 20
}
orc_warchief = {
    "name": "Orc Warchief",
    "max health": 75,
    "health": 75,
    "gold": 50
}
skeleton = {
    "name": "skeleton",
    "max health": 25,
    "health": 25,
    "attack": 10,
    "gold": 10
}

ghoul = {
    "name": "ghoul",
    "max health": 35,
    "health": 35,
    "attack": 12,
    "gold": 14
}

ghast = {
    "name": "ghast",
    "max health": 50,
    "health": 50,
    "attack": 17,
    "gold": 30
}

zombie = {
    "name": "zombie",
    "max health": 40,
    "health": 40,
    "attack": 5,
    "gold": 5
}

Necromancer = {
    "name": "Necromancer",
    "max health": 100,
    "health": 100,
    "attack": 0,
    "gold": 150,
    "alive": True,
}

Apprentice_of_the_Lich = {
    "name": "The Lich's Apprentice"
}

Pine_Forest = {
    "name": "Forest",
    "description": "You are surrounded by trees.",
    "exits": {
        "north": "cave",
        "east": "village",
        "south": "clearing"
    },
    "art": r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⠉⠉⠉⢢⠤⠤⡀⢀⣀⣀⠀⡠⠖⠋⠉⠉⠒⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠙⠄⠀⠀⠀⠀⠀⠈⡇⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠐⠠⠄⡀⠀⠀⠀⢀⠄⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠹⠔⠒⠢⠇⠀⠀⠀⠀⠀⠀⠠⠤⡖⠁⠘⡄⠀⠀⠀⠀⣠⣃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡠⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠰⡄⠀⠀⠈⠁⠀⠙⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⠀⠀⠀⠀⠀⡜⠂⠲⠀⠀⠀
⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⠉⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⠀⠀⠘⠒⠂⡀
⠀⢀⡠⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠘⠂⠈⠆⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⡝
⢠⠋⠀⠀⠀⡠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢄⣀⣀⡠⡂⠀⠀⠀⠠⡄⠀⠀⢀⡀⠀⢀⡰⠃⠀⠀⠀⠺⣅
⡇⠀⠀⠀⠀⠣⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⡄⠀⠰⣀⡠⣀⠀⢀⣠⠎⠉⣹⣀⠀⠀⠀⠀⠀⣸
⡇⠀⠀⠀⠀⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⢷⠒⠂⠐⡎⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠁⠀⠉⢢⠀⢰⠊⠁
⠘⢤⡤⠀⠀⠀⠑⠂⠐⢆⠀⣄⣀⣀⠀⠀⡀⢀⡴⠀⠀⡧⣀⠜⠑⠂⢺⢳⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡜⠐⠃⠀⠀
⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢎⠀⠡⠀⠀⠱⡀⣠⠀⠀⡏⠈⢱⢲⠂⠀⠀⠀⠀⠀⠀⠀⠀⠱⠀⠀⠀⠀
⠀⠱⣄⡀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠉⢫⣁⢫⡳⢄⢣⠀⠀⠉⠀⠀⢰⠇⢀⠇⢾⡻⠖⢖⠁⠀⡀⡀⠀⢀⡼⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡀⠀⠀⠀⠐⣄⣀⣀⡠⠎⠓⢯⡀⠀⢸⠀⠀⠀⠀⠀⣸⢁⠎⡴⡋⠀⠀⠀⡉⠉⠀⠈⡏⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠒⠒⠒⠋⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⣿⢏⡾⠝⠓⠢⠤⠊⠈⠑⠒⠊⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⡠⠄⣀⣿⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢸⡜⣉⢿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠸⡱⡻⡸⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡤⢄⡀⠀⢀⣀⣀⢇⠀⠀⠀⠉⠈⠀⡎⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⢤⡤⠀⢘⡆⠈⠋⣑⣽⣾⠌⠀⠀⠀⠀⠀⠀⠣⣸⣄⠀⢹⡅⠀⠔⠪⠿⢤⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⠈⠉⠀⢀⣤⣖⣋⣁⣀⣋⣀⣀⠀⠒⠒⠄⠀⠀⠈⠈⠓⠦⢤⣀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠦⣄⣸⡟⠒⠒⠒⠒⠒⠚⠛⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶'''
}

cave = {
    "name": "Cave",
    "description": "A deep, dark cave with many bats.",
    "base enemies": [copy.deepcopy(goblin)],
    "enemies": [copy.deepcopy(goblin)],
    "exits": {
        "south": "forest",
        "north": "inner cave"
    },
    "art": r'''
⠀⠈⠈⠈⠁⢀⢀⣰⢐⢲⠔⡂⡠⠀⡐⠀⡀⠔⠦⠀⢀⠲⠃⠁⠀⡀⠣⠄⢡⢀
⠀⣁⠴⡔⠀⠀⠠⢨⠈⠐⠏⠈⠃⠉⠀⠈⠀⠀⢐⣤⢕⣁⣞⠶⡏⠃⣈⡂⢧⠲
⠀⠯⠡⡂⠀⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢁⢔⣳⡾⣜⡐⡁⡐⣃⢀⣴⡍⠱⠼⢛
⠠⡄⠁⠐⠈⠠⠀⠀⠀⠀⠀⠀⠀⣠⣔⢾⣳⣡⣅⣴⠉⢂⠷⠁⠲⣴⠀⠅⢁⣿
⢀⢡⠈⠈⢐⡄⠀⡂⡔⡄⢐⢩⣽⣟⣂⣢⣟⢙⡜⣎⡊⡏⠃⡐⢫⡋⣀⣡⣽⢺
⢈⢶⠞⡇⣈⠃⠘⠁⢶⣷⡸⢎⠇⠻⠹⣟⠈⡞⢀⠋⠃⠀⡾⢿⣾⡿⠟⠟⠆⢰
⠁⠆⢫⡟⡈⠁⢄⠔⢩⠻⠱⡑⠃⠘⢥⣧⣀⡽⣂⠦⢍⣸⢩⡻⡤⡐⠀⠀⢤⣼
⠀⢂⡕⡳⡋⢅⠃⣵⡧⣯⡽⠃⡠⣫⣿⣿⣿⣻⣏⡿⢊⠃⡄⡆⡯⠈⠈⡾⠀⢸
⢆⢸⣞⢢⡵⢯⡘⠤⡲⣏⠑⣶⣾⣿⣿⣿⣿⣿⣿⣖⠄⠿⣑⠐⡞⠀⢸⡟⠓⢝
⠈⠏⠭⡐⣭⠍⡤⡾⡷⣧⣶⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⡄⡗⠀⢅⠉⡠⣷⢠⡸
⠔⡤⢠⣽⡩⣟⠡⡾⠠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⡇⢘⠈⢴⣷⢰⠀
⠕⠐⢰⢜⢳⠵⢂⡽⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢸⢃⢪⣶⣴⣀⠫⢎
⢄⣪⣾⣚⠾⠀⢒⡔⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡜⠿⠘⠧⣤⣖⢂⡻
⢓⠉⣉⡁⠀⣴⢃⠈⠌⣸⢿⣿⣿⣿⣿⣿⣿⢿⠿⠻⠇⢍⠳⡶⢴⡿⢿⣉⣗⡹
⠀⡅⢀⠀⠀⣼⡆⡂⢆⣅⡷⡀⢁⣠⢃⡙⢁⠠⡅⠠⠀⡁⢀⣐⢤⡀⣼⣱⠯⣌
⣗⣰⣰⡔⠒⢱⡈⠐⢨⣾⣡⣵⠈⠁⣤⣄⡀⠀⠀⣉⡉⠀⣳⢩⣌⣼⡕⣮⣷⣞
⡿⣻⡹⡱⣿⡻⡻⢷⠸⠙⠙⠃⠀⠀⠉⠈⢁⠰⠀⡏⢻⣳⣱⡿⢉⡇⢻⣋⡎⠿
⢦⣡⡛⡝⣞⢥⠓⢡⢖⢀⡂⠠⠄⣀⡀⠀⣈⡀⠤⡊⣊⣾⣴⣣⣵⣤⠫⣓⣯⣾
⢫⢿⣯⠿⢄⡲⢖⡴⢮⡓⠂⠀⠀⠒⠀⠠⠄⠀⠡⠜⢏⡌⢻⣸⣥⣟⢇⡽⢮⣻
⣺⣢⡮⡃⠂⠑⠐⡣⠚⠉⠀⠀⠀⠀⢂⣴⢇⡭⠇⣾⢟⢪⡤⣸⡿⣷⣿⣥⣯⢾
⣶⣤⣮⣤⣴⣤⣴⣬⣤⣤⣤⣤⣤⣤⣤⣤⣼⣤⣤⣯⣶⣷⣯⣷⣿⣿⣯⣿⣼⣿
⣿⣧⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿'''
}

inner_cave = {
    "name": "Inner Cave",
    "description": "Deeper into the cave, where there is little sunlight",
    "base enemies": [copy.deepcopy(skeleton), copy.deepcopy(goblin)],
    "enemies": [copy.deepcopy(skeleton), copy.deepcopy(goblin)],
    "exits": {
        "south": "cave",
        "north": "The Depths"
    },
    "art": r'''
⣧⣿⠏⣻⣳⣣⣗⡯⣐⠇⣼⢥⡽⣚⢖⠠⢃⠰⠌⣦⠀⠀⠌⡠⡴⡀⢐⠸⠘⠀⣬⠁⠁⢂⠄⠠⠀⠂⠡⠀⣜⠴⣠⠠⠌⠆⡀⢀⣃⡈
⣞⣹⡶⣾⣧⣥⢻⢘⣍⠷⡏⣗⡮⢠⡾⢶⢀⠰⠈⡿⡀⢰⢸⠃⣮⠧⠂⢰⠀⡆⡾⠘⠀⡐⡦⡜⢰⠄⢐⢠⠈⠔⠁⣝⡦⡇⠀⡌⢤⢉
⡽⡡⠑⣿⡷⣾⣽⡪⣟⡉⣯⡟⡇⣟⡣⣥⠀⡇⡙⢃⠣⠜⣌⢀⡙⢈⢠⠃⢸⡈⢥⠀⢤⡇⠁⢡⢺⠈⢌⢘⡀⠫⠼⣇⢂⡑⠆⡟⡈⡎
⢒⣳⣶⣿⣽⣛⣶⣷⡏⢳⣿⠗⢣⢸⣸⢹⠃⢉⠑⡀⣰⡇⣿⢸⣜⠀⡆⡁⣠⡟⣍⣞⡵⢵⠒⡌⠠⠤⠀⡞⡀⠈⠑⡞⢈⡑⠋⣷⡸⣁
⣧⢻⢽⠻⣿⣫⣟⣟⣧⢥⡊⣧⣇⡦⡹⣻⣰⢻⠀⣜⣯⣫⠕⡋⢽⡀⡏⠐⣸⡏⡾⢗⢤⣺⡀⠑⠠⡆⠀⢠⠃⠈⡜⢈⢧⢇⠁⣟⡷⡻
⢃⣊⡒⡬⡳⢓⢻⠏⠟⡞⡅⠱⣍⠲⢏⡵⣮⡿⢁⣯⣒⡤⢚⠽⣣⣻⡃⢸⢧⡞⡭⣭⣃⣶⡇⢰⢘⡇⠂⣘⠀⠐⡈⢆⠸⢸⣿⡀⢤⠢
⢎⣏⠐⣡⠐⠭⢌⡍⢠⡇⠃⣌⣹⣽⣟⢴⢠⡾⣽⣿⡾⣾⡟⣭⠷⣼⢡⣼⢋⠾⣉⡴⡞⡴⣮⢼⠉⣷⢠⢹⡖⢀⠒⡌⠢⣿⣿⢃⣦⣷
⢼⢢⢉⠤⢈⠺⢨⢲⣻⠀⠠⣸⣿⣷⡏⣾⣾⣿⣽⣻⣿⡿⣧⣿⣾⣿⣧⣎⣏⣷⣦⡣⣹⣟⡇⢸⠈⣻⡏⣼⣇⠈⠰⣈⠱⣿⣿⣿⣿⣿
⣿⣜⣳⠇⣾⣷⣿⣿⡿⢻⠀⣿⣾⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⡟⣿⢿⣿⣇⣸⠃⡼⣃⣿⣧⢀⠇⢠⢿⣿⣿⣿⣿⣿
⣟⢎⣹⢟⡾⣿⢿⣿⡷⣞⢻⢹⣿⣿⣻⣿⣿⣿⣿⣿⢿⣿⣿⣿⢿⣿⠁⢻⣟⣻⢿⣿⣿⣿⠏⢱⢳⢃⠏⢻⣿⢘⠰⠎⠻⣿⡿⣿⣿⣿
⣚⣠⢥⣰⣿⣷⣺⣶⣽⣿⢿⣾⣻⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡏⢁⣿⣿⣿⣌⣉⣥⣶⠃⢸⡡⡇⠀⢸⡯⠈⠀⢨⠑⢿⣿⣿⣿⣿
⢝⢮⣝⡺⣶⡿⣽⣛⣿⣿⣿⢿⣷⣿⣿⣯⣿⣿⣿⣟⣿⣿⣿⡏⠐⠀⠈⣻⣿⣿⣿⣿⣿⣿⡃⠬⣔⡇⠀⢸⡗⡀⠱⠀⠌⢂⡟⠂⢿⡿
⡽⣲⢩⣞⣿⣽⣻⣷⣿⣿⣿⣻⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⠇⣐⣈⠍⠙⠿⣿⣿⣿⣿⠟⢁⠈⢫⡁⡄⠀⡂⠀⠈⠠⢘⠫⠹⠉⣁⣩
⣽⠡⢯⢿⣟⣯⣏⢳⡝⠏⠙⣿⣽⡿⠿⣯⡤⢪⣟⡇⢨⣿⡇⠐⢠⡬⢌⠠⡀⢽⣿⣿⢿⢢⠀⠀⠈⠎⠣⠘⠚⠃⢃⣡⠖⠖⠏⠙⠌⠤
⣿⢷⣹⢮⣻⣴⣯⡾⡆⠀⢠⡼⠋⢀⣼⠡⡘⠁⢀⡀⠀⠒⢂⠆⢸⠀⠠⡉⠵⢔⠉⠄⢢⠉⠁⠀⠀⢐⡀⢅⠌⣐⢢⠌⠃⠭⠀⣀⠀⠀
⢿⡟⢻⢾⡿⣿⢳⣷⠃⠒⡏⠠⠄⣹⠉⡸⠒⠠⠁⠀⠈⠀⠐⠀⠀⠀⠀⠈⠁⣸⣦⢦⣋⠀⡌⢁⡉⢢⠔⣠⠤⣆⡦⠟⠊⠉⠉⠀⠀⠀
⣾⣶⡗⣶⣻⢽⡿⣊⡀⣀⡅⢣⢒⡥⠢⠁⠠⢁⠀⡀⠀⠀⣀⠦⠐⢆⠠⠬⣝⣁⡶⠘⠚⠻⠊⠃⠚⠃⠘⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡽⣧⣟⡞⣛⣫⣷⡳⠷⡋⣔⣀⣠⠤⠢⠤⠕⠢⠖⠊⠃⠘⠑⠊⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠡⠉⢳⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣠⣤⣂⣖⣶'''

}

The_Depths = {
    "name": "The Depths",
    "description": "The deepest, darkest part of the cave. Or is it?",
    "base enemies": [copy.deepcopy(Necromancer), copy.deepcopy(skeleton)],
    "enemies": [copy.deepcopy(Necromancer), copy.deepcopy(skeleton)],
    "exits": {
        "south": "inner cave"
    },
    "art": r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠘⣀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢲⣿⣿⠓⠁⠀⠀⣰⢆⡇⢆⠓⡰⢇⢶⣥⠾⣐⢞⣬⣷⢒⣜⠺⠧⢚⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠄⠗⡤⡀⠠⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢸⣿⣿⠜⠋⠁⢀⢀⠆⢀⡏⡞⠯⡤⣋⠷⣬⢞⡰⡯⡇⣾⡝⡼⡱⢧⢾⡼⢃⡄⢁⡐⠂⠠⢀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠌⠀⠀⠀⠀⠀⠀⠐⠀⡀⠄⠀⡌⠄⡅⢐⠆⡅⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⢻⣸⠁⣛⠀⠀⠀⣨⣬⠆⣼⣰⠁⢿⡵⣟⣰⣥⣾⡇⢓⢃⡇⣿⡟⣹⣋⢉⣿⡧⡄⠂⠀⠂⠁⡀⠀⢀⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠠⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⡰⢰⡁⠎⡓⠀⠀⠀⠀⠀⠀⠀⠰⠆⠀⡀⣩⠼⠃⡴⠀⡼⢁⣽⣾⠝⣠⡾⣿⢳⢧⡧⣞⡽⢶⠟⢀⡞⠱⢁⠿⣸⢼⣿⣴⠡⠀⠄⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠆⠀⠀⠀⠆⠀⠀⠀⠠⢀⠐⠀⡁⡆⠏⠂⠘⠀⠀⠀⠀⠀⠀⠀⠀⣁⡀⠆⢨⣿⢠⠜⢡⡜⣰⢣⣿⠁⢀⣸⢿⣟⡿⣞⡽⣫⣷⠈⠀⣾⠠⡏⣄⡇⡿⠟⢁⣰⠨⣑⠂⢈⡀⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠠⠂⠀⠀⠔⠀⠀⠊⠆⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠤⠃⠁⠉⠀⢠⡞⢽⠃⣿⣶⠻⡄⣿⠟⢻⣾⢷⣯⢳⡯⠉⠀⠀⣬⠐⢰⢻⠃⠁⠰⠏⣭⡅⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠠⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢠⠀⠀⠀⠀⣴⣦⣾⣿⣿⠾⠿⣏⠀⢀⡷⢏⣠⣿⢏⡼⣹⡿⠁⢀⠀⣠⡏⢠⡌⠀⠀⠀⢀⣤⣄⡀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⣀⠒⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠉⠀⢀⠀⠔⢠⡙⠿⠚⠀⠀⢀⠁⣶⡟⣷⢟⣾⣿⠟⢘⠿⠁⢰⠃⢈⣿⠂⠈⠁⠀⠀⠂⠀⠁⣉⡛⠛⠁⠐⠚⢉⣉⣘⠃⢒⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠄⠈⠈⠡⣤⣉⢳⠀⠈⠙⢿⣦⣤⠾⢁⠾⣞⣾⡽⢻⠗⢁⢆⣿⡃⢀⠏⠀⠈⠀⠀⠀⠀⠀⠀⠂⣚⣷⣬⣝⢡⣤⣤⣶⢯⣉⣉⣿⣄⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠐⠀⠀⠀⠀⠀⠀⠀⢦⠀⠀⠀⠀⠀⠀⢦⡆⠄⠞⡱⠆⠃⢉⢀⣁⠀⠌⣩⣤⡖⢻⠟⠩⣴⡰⢋⣤⣿⡯⣾⠁⠊⠀⠀⠀⠀⠀⠀⠀⠈⣤⡜⠿⣽⣷⣿⣾⣷⣞⣾⡡⠏⡉⣥⠜⠩⠇⢣
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠼⠀⠀⠀⠀⠀⡄⠀⡄⠽⢠⠀⠉⠀⢀⠦⠆⢀⠃⣴⣈⣵⣿⣢⠀⢰⢋⢁⣮⣿⣿⣾⠁⠀⠀⠀⠀⠀⠀⣀⠂⠀⣰⣿⣿⣷⣶⡶⡦⣵⡽⠏⣫⣷⣶⣔⣠⡚⠀⠘⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⡀⠐⠀⠀⠀⠀⠀⣤⠂⣠⠱⠀⠀⡸⢈⡇⠀⠀⠈⠀⠐⠂⠆⣱⣯⣽⣿⣿⡁⣾⢏⡘⡹⣳⡞⠃⠀⠀⠀⠀⠀⠀⣰⡥⠏⡀⣿⣿⣿⣾⣿⠛⣯⣿⡡⣠⣿⣅⣯⠜⡄⠅⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⢠⠀⠀⢀⡄⠀⢆⠁⢸⡆⠀⠀⠃⣘⡃⠀⠀⠀⠀⡀⣴⣿⣿⣿⣟⣎⣿⣁⣿⠾⣾⡓⡡⠀⠀⠀⠀⠀⠀⠈⠀⠄⣡⠌⢡⣿⣿⣿⣿⣿⠄⢀⡴⢗⡄⣟⢺⡖⢫⠒⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⡘⡄⠀⣾⠀⠀⠠⠀⢈⠠⠀⢀⡙⠅⢶⠀⠀⠀⡀⠀⠙⠘⢿⣿⣿⠁⠈⣏⣵⢶⠟⠀⠀⠀⠀⠀⠀⠀⢠⠀⡾⡿⡁⣺⡼⢿⣿⣯⡻⣿⠀⣄⣴⢿⠃⣿⢣⡟⠢⠅⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡘⠆⠀⠀⠈⠀⠀⢀⡇⣠⠀⠗⠀⢠⡌⢈⠀⠑⠄⣄⠑⠀⠈⠆⠀⢰⠬⠇⣀⡀⠀⣿⠁⡄⠀⢻⢩⡃ ⠀⠀⠀⠀⠀⠀⢀⡞⣰⠟⠁⣸⣿⣾⣼⡿⣿⣟⡦⣟⣯⣽⣇⠀⣿⡾⣎⡱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⠀⠀⠀⠀⠈⠃⠈⣄⠀⣦⠙⠙⠶⠀⡀⠀⢐⠀⠀⠀⠁⠀⠀⣦⡐⠏⣉⠲⠏⠴⠁⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⣡⣞⣿⣯⣿⣿⣿⣿⣿⡿⡝⢭⡼⢿⡿⢸⣧⡽⣝⡲⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠃⠀⠀⠘⠄⢻⣦⡀⠀⠀⠸⠄⠈⠀⠀⠀⠀⠀⠁⠀⠃⠈⢠⣬⢿⣷⣾⣧⣬⡄⠀⠀⠀⠀⠀⠀⢀⣶⣾⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢍⡧⡘⣿⡇⣸⢲⣹⣓⡌⢂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⢀⠆⠰⠀⠀⠀⢸⡄⠂⠈⢀⡀⢸⠊⣵⣿⠀⡖⢦⡰⠆⠀⠀⠀⠀⠈⠀⠀⡸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡄⠁⠀⢀⣾⣿⡟⣀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣈⠲⣁⣿⡆⣻⢱⠹⡖⠧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠜⣧⠆⠀⠈⡄⠐⠃⠠⠀⠈⢶⣶⡆⢸⡟⠵⠮⢷⡏⠜⡄⠀⠀⠠⠈⠀⢠⠀⠈⠉⠈⠻⢿⣿⣿⣿⡎⢿⣯⠠⠀⢰⣿⠿⢡⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠧⣧⠒⠁⢮⠁⣯⠘⡭⠙⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣴⠉⡄⠀⠀⢠⠀⡀⢁⢄⠀⢸⣿⣧⡈⠉⠶⡴⣌⡷⢀⠀⠀⠀⠀⠀⠀⢦⣉⢷⡄⠀⠀⠈⢿⣿⣿⣿⡄⢿⣆⣆⠈⣤⢠⣿⣿⣿⣿⣿⣼⣿⣿⡿⣿⢿⡄⡇⢆⣈⠀⢰⡈⠰⡀⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⡀⠋⠀⠇⣀⠀⠈⠄⠈⠢⠀⠃⠈⢿⣿⡏⣷⡄⠘⠛⣧⡈⠁⣈⠂⠀⠀⠀⠈⠊⠃⢷⠀⠠⢰⠀⠻⣿⣿⣿⣼⣿⣷⣶⣿⣾⣿⣷⣿⣿⡿⣫⣾⣻⣾⡿⡿⠈⠦⡘⢀⠃⠄⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⡄⠀⠀⠀⡆⢰⠀⠀⠉⢆⠀⠀⢀⠀⠀⢠⣀⣌⠻⢧⠐⣆⡈⢻⡤⡴⢐⡾⢇⡆⠀⠠⠀⣀⢀⡀⠀⠀⠈⠁⠀⠻⠿⣿⣿⣿⣿⣿⢻⣿⣾⢿⣿⣋⣜⣻⣫⣿⣻⣶⡙⢠⠓⠠⢃⠀⠄⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡔⠀⠀⠀⡂⠸⠃⡆⠣⠀⠀⠀⠀⠀⡀⢄⢻⢿⣧⠸⡷⢆⢨⣀⠙⢗⡌⠆⠋⢫⠀⢤⣤⣆⣬⣿⠃⣄⡀⠀⠀⠀⠀⠈⠹⣿⣿⡿⣿⣿⢿⣾⣯⣿⣿⣿⣿⢟⣹⠿⡱⢀⠉⠒⡌⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⡄⠀⠀⠀⡇⠀⠀⠀⡇⠰⢀⢉⠀⠀⠀⠰⣄⠈⠙⢀⠀⡂⠹⠀⠉⠛⠀⠙⠀⠀⢙⣳⠈⢃⠜⢦⡵⣯⣽⢯⣿⣝⣿⣷⡔⢰⠀⠀⢠⠈⡿⠁⠉⠁⢠⣾⣿⡿⣿⣽⡟⢼⡳⠢⡅⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠁⠀⠀⢠⠉⠀⠀⠀⡇⠀⠀⠀⡀⠀⠰⢀⠀⠀⣀⠀⠼⠀⠁⢆⢰⣿⣿⡇⠐⢀⠀⠀⢀⠀⠀⠞⠀⠌⠎⣵⢼⣍⣋⢬⡙⠻⠾⣷⣿⡀⠀⠀⠾⢸⠃⠀⠀⠀⣾⠿⠿⡿⠛⠋⢩⣤⠂⠐⠀⢁⡀⠀⠀⠀⠀⠀⠠⠀⠄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢶⠂⢀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⢠⡈⠀⢠⢠⢰⡌⢠⠛⠟⣿⣾⣿⡦⠈⠛⠔⠈⠂⠀⡸⠀⠋⠉⠿⢛⣶⠟⠃⠑⠈⢈⡻⠆⠀⠃⠙⠀⠂⠀⠂⠀⠠⢤⠀⠀⠉⣀⠙⣿⢃⣀⡈⠙⣢⣌⡓⠄⠡⠀⠉⠂⠀⠀⠀⠀⠀⠀
⢀⠀⠀⠓⠃⢀⠀⠀⢠⠀⠀⠄⠀⠀⠀⠀⠀⠀⢠⣾⠰⣌⠰⡇⠀⠀⠀⠁⡢⠀⡇⠀⠄⢸⡇⣶⣆⢨⠌⣇⠠⢼⡒⢯⠥⠟⢿⡀⠀⡄⠂⠀⠀⠦⠐⠄⡀⣘⠏⠀⠀⠀⠀⠀⢀⡉⠀⠰⡄⣡⣄⠀⠀⠀⠀⠀⠀⠐⠠⠄⠤⠤⠤⠤⠉⠁⠠⢭⣥⣤⣠⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣧⢻⠓⡀⡄⣀⠀⠸⣆⠠⠀⠀⠀⠀⠈⠀⠀⢸⣯⡁⠯⡔⠃⣀⠀⢀⠁⡇⢀⡇⠀⠇⠘⢰⣿⣿⣮⢀⠋⢸⣾⡇⠸⠅⢀⠠⡄⠀⢀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢀⠀⠀⣸⠀⠈⠸⣿⣙⣿⠁⠂⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣄⠀⠀⠉⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⡹⣿⣾⡞⣃⢸⣷⢆⡀⠈⠀⠀⠀⢀⠀⣌⠀⠀⠐⣯⠀⣀⠀⣿⣇⠀⠀⢐⠇⢸⠁⢾⡇⢀⠘⡿⠏⠻⠟⠉⣀⠀⠂⢠⣤⠁⠀⠀⠀⠀⠀⠀⠀⠀⡾⣷⡆⠀⠀⠰⢶⡿⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠋⠀⣄⡲⢶⡦⣀⠀⠀⠈⠚⣡⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⡄⢙⣷⣎⠈⣿⡌⠁⡄⠀⠀⣴⣧⠀⠈⢐⠀⠀⣿⠀⡟⠀⣿⢷⠁⠀⠸⡇⢸⠀⠿⠇⠙⠀⠁⠁⠀⠈⠓⠙⠗⠀⠈⣥⠐⠆⠰⠂⠈⠀⠀⠀⢠⡀⢤⣤⡀⠀⠄⠀⠙⠆⠀⠀⠈⠉⠀⠀⠀⠀⠀⣀⠀⠀⠀⠐⡿⠏⠈⠀⠉⠉⠀⠀⠀⡈⠉⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣿⣿⡀⡏⢿⠀⠇⠀⠈⠙⠑⠀⠀⠈⠀⠀⠈⠀⠃⠀⠙⠘⠀⠀⠀⠀⢈⠀⠀⠀⠀⠀⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠹⢛⠋⠊⠀⠀⠀⠀⠀⠀⠀⡀⡀⠀⠀⠀⠄⠀⠀⠉⠠⠶⢚⠛⠃⠑⣀⠀⠀⠀⠂⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣤⢰⠶⠉⠛⠃⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠀⠀⠀⠀⠀⠁⠀⠀⠠⣤⠄⠀⠤⠀⠀⠢⢠⡄⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠠⢴⡆⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⠀⢀⡀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⢀⡀⢁⡀⠀⠀⠀⠀⠀⣀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⣀⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠆⠶⣀⢠⡄⠀⢤⠀⠀⠀⡀⢰⡀⢀⣀⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠉⠉⠁⠀⠀⠀⠁⠀⠀⠢⠇⡌⠲⠘⠀⠀⠁⠀⠀⠠⠂⠉⠁⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⡄⠀⠁⠀⠀⠁⠐⠀⠊⠑⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣂⠂⠉⣮⢁⠀⠀⠠⠌⠀⠔⠀⠄⠀⠈⠇⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠄⠃⠈⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡿⢻⣿⠂⠀⠀⠀⠀⠀⠑⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠘⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⠃⢻⢻⣿⣞⣿⡇⠀⠀⠀⠀⠀⠀⠈⢋⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢻⣿⠿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢴⠙⠆⠈⠀⠀⠈⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
}

village = {
    "name": "Village",
    "description": "A small village.",
    "exits": {
        "west": "forest"
    },
    "art": r'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡿⣰⣄⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⠆⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠸⣿⠋⠐⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠀⠀⠏⠀⠀⢤⢤⡀⠀⠈⠛⠿⠛⠛⠉⠁⠀⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠀⠀⠨⡀⡀⢺⠑⠀⣁⠀⠀⠀⠀⠀⠀⠀⡈⠁⣿⣿⣿⣿⣿
⣿⣯⡿⠿⢏⢀⠄⠠⠀⠀⠀⠀⠈⠠⠀⠀⠈⠀⠀⠀⠀⡀⣆⠂⠀⣸⣿⣿⣿⡟
⠟⠉⠀⠀⠀⠀⠀⡀⡀⠀⠀⠀⠀⠀⢀⠈⡀⠰⠠⢠⠀⠀⠈⠠⣀⣠⣿⣿⣿⠓
⠀⠀⢦⡕⠀⢀⠀⠀⠀⠂⠀⠀⢀⠀⠀⢈⠐⢀⠘⠀⢨⢠⠀⡀⠀⠙⠉⠋⠛⠀
⠀⠀⠈⢫⠃⠀⠀⠀⠀⠀⠂⠀⠀⠀⠂⠀⠀⠀⠀⠡⢂⠄⠀⠃⣤⡂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠈⠁⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠄⠠⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠀⡄⢀⠒⠰⠀⠄⡂⢂⠈⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀
                                    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠄⠀⠀⠀⠀⠠⣑⣭⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⡄⠢⡩⠀⠀⢠⠀⠀⠁⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⢠⠀⠀⠀⠌⠳⡂⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀
⢀⠀⡄⠐⡀⠠⢀⡀⢀⠀⡀⢀⠀⠀⠀⡀⠀⡀⢈⠀⠀⢀⣀⡀⣄⢀⣄⡨⢄⡠
⠤⠃⢈⠆⡄⠃⠄⠐⣈⣀⠓⠂⠙⡠⠱⠰⢢⠨⣄⢹⢑⢑⠾⣂⣇⢇⢟⢜⢍⣵'''
}
clearing = {
    "name": "Clearing",
    "description": "A small clearing in the trees.",
    "exits": {
        "north": "forest",
        "south": "Deep Forest"
    },
    "art": r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡤⠀⠠⠀⠀⣄⣀⣀⠁⠃⢠⣿⣿⣄⠀⣿⣿⣿⣿⣿⡣⡐⣥⡔⠁⢀⠄⠂⠀⠀⠀⠀⡀⠀⣀⢀⠀⣇⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠂⡹⠧⠋⠀⢰⡳⣯⣯⡛⡿⢿⣿⣿⣿⣿⣿⣼⣿⣿⢾⣯⠄⠀⠄⠀⠀⣠⣿⣮⣍⡁⠀⠸⡄⠀⠂⠢⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢂⠐⡀⠂⠀⠀⢀⣠⠶⣷⡗⢽⠏⣿⣗⠿⣿⣿⣿⣿⣿⣟⣵⡯⣗⢑⡥⣵⠾⡶⣭⢣⡩⠕⣻⠀⠀⢳⡦⠀⠱⠠⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠊⣭⢃⡚⣬⣗⢾⣿⡎⢟⣿⣪⡽⣿⣿⣿⣿⣿⣿⣿⣬⣿⣿⠾⠻⣾⢓⠗⠎⠒⡀⠀⠀⠙⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⣞⡈⢤⣨⡅⣂⣲⣮⣓⢟⢺⣷⡝⡷⣻⣿⣣⢿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠿⢫⣿⠪⣍⡟⢻⠥⡁⢄⡀⠀⠀⠀⠀⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡐⠌⢃⠞⠀⠫⠂⣔⢫⡛⣖⣹⢏⣟⢿⣿⡷⡹⣟⡵⣳⢻⣿⣿⣿⣿⣿⣿⣿⣏⣈⢪⠿⠓⡑⣬⡟⣄⣵⠢⠌⡤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠈⠀⠀⡀⢲⢠⠓⠺⣔⢯⣽⣰⣍⡤⢟⣛⢿⣾⣿⠟⢾⣭⡝⣿⣿⣿⣿⣿⣿⣿⣯⣔⠇⢌⢾⠏⣙⠋⣌⠁⢣⢂⠡⠈⠲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠠⢁⢔⢈⠃⡌⢋⠈⢛⠟⡊⠝⢭⣻⡿⣦⢫⣿⣝⢿⣿⣾⣿⣫⣻⣿⣿⣿⣿⣼⢿⣹⣻⢊⣬⠓⡌⡰⠈⠄⢢⠠⠁⠂⠄⠉⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠘⠌⢀⠀⠈⡀⠙⠏⠋⣼⣹⢿⠃⣄⠟⣧⣹⡁⢿⢿⣿⣿⠿⢸⣿⣿⣿⡟⡤⠹⡡⡇⢻⢣⠡⠘⠀⠁⠈⠀⠀⠁⠈⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⡀⠄⠀⠇⢤⢁⠈⠁⠠⡄⢄⠶⢇⣿⢾⣿⣿⣼⣏⣼⢿⢠⢎⡧⣿⣶⡦⣹⣿⣿⡧⣷⣆⠧⡄⡼⢦⡀⠤⡈⠀⢀⠀⠄⡀⠀⠀⡀⠄⠀⠀⠄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠄⠠⠁⠒⠤⢂⠠⣉⠔⡐⠬⠸⢆⡓⣪⣾⢷⣧⢿⣿⣷⡼⣙⢥⣮⣏⡻⣚⣟⢿⣯⣿⣾⢶⡏⠝⣻⠆⠑⡫⡙⣄⠘⢋⡐⢠⠀⠀⠒⠈⠄⠈⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠩⠈⠄⠆⢁⠂⠡⠈⣄⠢⠞⠠⠓⣌⠲⡙⢏⠫⡕⡎⣯⣯⣿⣗⡿⣿⣛⡿⢽⢵⣿⣿⣿⣿⣦⣞⠇⣳⣒⢭⢂⡑⡠⠸⢤⠦⡀⠂⠀⡀⢀⠀⢐⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠍⠬⠘⠐⠈⢠⢦⠰⠉⢀⢃⡍⠬⠱⡘⣬⡷⣞⣰⢝⣟⣿⠗⣝⣿⣪⣮⡗⣾⣿⣿⣿⡟⣿⣿⢟⢿⡳⠛⡛⢢⠡⣁⠈⠙⣁⠀⠀⠐⡀⠂⡀⣶⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⠀⠀⠠⢠⠄⠀⠀⠘⠋⢀⠖⡨⢖⡬⢃⡣⢉⠻⠽⣳⢂⠝⢜⡯⢻⠭⢺⣿⣷⣷⣿⡿⣿⣻⣿⢿⣞⡿⣌⢪⢰⠉⢆⠱⣀⠒⡀⠄⠀⢀⠀⠀⠐⠠⢰⢣⠀⠀⠀⠀⠀⠀⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡯⢳⡀⠀⠈⢢⠀⠀⠂⠠⢀⢀⣭⣉⠤⣍⣪⣭⣎⡡⣿⣦⠃⡷⣨⣶⣿⣿⣿⣿⣿⣿⣟⣯⣿⣽⢻⣚⡽⣩⢖⢡⡚⡄⢣⠄⡬⢦⣥⣌⠀⠀⠀⠈⣔⢃⢆⠀⠀⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⢻⢡⣓⡠⡀⠐⢀⡀⠈⠀⠄⠂⢩⣶⣾⣿⣿⣿⣽⣯⢻⣜⠇⡜⢰⣿⠿⢫⣻⣟⢿⣿⡿⡽⡝⣞⡱⢣⢞⣵⠑⣨⣾⣼⡻⢄⠁⠰⣿⣿⢿⡀⢀⠀⠀⢿⣿⢡⠣⠀⠀⠀⠀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡼⢡⣿⡱⡄⠀⠁⠂⢁⠈⡐⢸⣿⡿⣽⡿⣾⣿⢫⣿⣿⡖⠸⡜⣡⣾⣿⣿⣿⣿⣾⣳⡝⣷⣼⢿⢃⣶⢁⢲⣿⣾⣷⣿⣾⣦⠀⠈⠳⠟⠀⠀⡀⠀⠘⣷⡝⡛⢁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⡻⢴⢫⡄⠀⠈⢀⠀⠀⡘⣿⣿⣿⣿⡽⣿⣟⣿⣿⡇⡼⢹⣿⣿⣿⣿⣿⣿⣛⢶⡻⣬⡑⠦⠣⡄⢢⣿⣿⣯⣿⣿⣿⣿⣷⣎⠀⢀⠂⠀⠀⠐⠀⠉⠀⡉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢏⢧⢡⢋⡍⠿⣆⠀⠂⠀⡀⠌⠹⣿⣿⣿⡿⣿⣿⢿⣿⠰⡱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣿⣷⡥⠜⡥⠹⣿⣿⣿⣾⣿⢿⣽⣿⡧⠀⠄⠀⠈⢠⠠⡄⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡀⠀⠀⠀⠀⠀⠀⠈⢆⠰⠦⠎⡭⢏⠀⠀⢁⠠⢈⠁⢻⣿⢲⣽⣳⢾⣿⡏⣱⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠨⣜⡡⠽⣿⣿⣾⢯⡯⢛⠺⠀⠀⠀⠀⠊⠀⠄⢂⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⠀⠀⠀⠀⠲⠆⠈⡆⠕⠎⡠⠃⡉⠄⠀⡀⢂⠀⠂⡹⣿⣜⡯⣟⣾⠰⣭⢞⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⡗⢦⡙⢮⢹⣞⠯⢏⡔⠃⠠⠀⠀⠁⢀⡄⣩⠐⠂⠸⡐⠀⠀⠀⠀⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠀⢸⣄⠮⡐⢀⠤⣌⠖⢖⠄⠠⢁⠤⢍⣻⣿⣿⢾⣝⣎⣯⢖⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣵⢣⣙⣦⣙⠾⣏⡞⠎⠂⠀⠄⡁⠠⠒⡐⡊⡼⠀⡉⢠⠃⠀⠀⠠⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠄⡀⠀⠀⠀⠨⣣⠀⡈⡐⢀⠒⢠⢂⡄⡁⠂⣄⡁⠺⠟⢿⡿⣿⢾⣿⣯⣼⡿⣽⢿⣿⣿⣿⣽⢟⣷⣾⢿⣭⡞⡏⠻⢉⢤⡤⠑⣈⠤⣈⡱⢡⠦⠔⡀⠌⣠⠆⠀⢀⠤⣀⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠙⠫⡦⠒⢧⡾⠤⠣⣞⣽⢹⣆⡟⢃⣛⣠⢈⢳⢋⢷⡳⡭⣝⣯⣝⡧⣶⡛⣯⣛⡛⠞⣭⠶⢴⢶⣧⠾⢴⠴⣵⣼⡸⠄⡒⣡⣌⠠⠡⠂⠁⠀⠈⠉⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠙⠐⠀⠀⠈⠞⠮⣀⣟⡭⣼⡩⣶⣟⣬⢶⢟⣔⣩⣖⡰⠤⢻⡗⣿⣿⣓⣷⣯⣿⣿⣴⣽⣼⣥⡼⡵⡶⡝⢛⠢⣣⠘⠀⢀⠂⡈⢨⠤⠂⠀⠀⠉⢀⠄⠀⠀⠀⠐⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠐⠂⠀⠀⠐⢎⠲⠢⣞⡗⣛⣶⣋⣕⣙⣿⣶⡿⣿⣿⣿⣿⣿⣿⣿⣛⣻⣿⣟⡭⠽⣯⠟⣴⢰⢴⠘⠟⣃⡴⡩⢛⠪⠽⠚⢆⠡⠀⠒⢁⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠔⠨⠄⠀⠀⠀⠀⠀⠀⠑⠒⡩⣍⣒⡽⠣⢲⣡⣯⣿⣿⣻⣿⣿⣿⣿⣿⣿⣭⣿⡷⠶⠦⢟⠛⠚⣯⠬⢶⢎⣭⣭⢶⣧⠭⢏⡙⠀⠀⠀⠀⢀⠀⠔⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠉⠃⠃⢿⡉⠛⠋⠉⣹⠀⢋⠹⠿⠏⣹⠙⠛⠻⠉⠀⢠⠄⠃⠠⡄⢠⠀⣁⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠀⡀⣀⠀⡄⢰⢀⢉⠿⢦⡼⣤⢴⣤⡄⠄⢄⣀⠠⣀⣀⣠⣄⣀⠁⢉⠧⠹⠶⣿⠶⢶⣤⣤⢿⣿⢷⣉⣷⣿⣾⠏⡷⠇⠌⡄⡉⣁⢀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠃⠘⢀⠂⠈⠀⣉⠎⣍⡒⢎⡛⡏⣒⢒⣶⣖⣝⡦⢶⣦⣴⡾⢧⣬⡵⡾⣿⣾⣯⣶⣶⣶⡙⢋⡠⠶⣠⢀⡑⡙⠌⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠤⡉⠂⡈⢀⠀⡈⢂⡉⠔⠢⠔⢬⢋⡍⣉⣉⡛⡟⢯⠩⠑⠏⠉⡛⡛⢩⡀⢤⠠⢤⡈⢁⠃⠈⢀⠀⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⢀⠀⠙⡀⠊⠑⠆⠒⢈⠈⡈⢁⠀⡂⠤⠘⢛⡛⢩⠠⢁⡘⢁⠌⠤⢋⠤⣐⠠⠦⣈⠦⠄⢄⠠⠂⡀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠈⠠⠁⠌⠀⠀⠈⠀⠀⠀⠀⠀⠀⠂⢁⠂⠡⠐⡈⠄⡐⢠⠑⠠⠘⠠⠁⠆⠠⠀⠌⠠⠀⠄⠈⠌⠀⠀⠔⠉⠀⠈⠁⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡀⠄⠀⠠⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠁⠈⡀⢁⠈⡀⠀⡈⠀⢀⠀⠂⡀⠂⠌⠐⠠⠀⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠐⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠂⠐⠀⠁⠠⠁⠀⠄⠂⠄⠡⠐⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
}

outpost = {
    "name": "Outpost entrance",
    "description": "The entrance to an outpost controlled by evil forces.",
    "exits": {
        "north": "barracks",
        "east": "Deep Forest",
        "west": "Command Room",
        "south": "Armory"
        
    }
}
barracks = {
    "name": "Barracks",
    "description": "The barracks of the outpost.",
    "base enemies": [copy.deepcopy(orc), copy.deepcopy(goblin), copy.deepcopy(goblin)],
    "enemies": [copy.deepcopy(orc), copy.deepcopy(goblin), copy.deepcopy(goblin)],
    "exits": {
        "south": "Outpost entrance",
    }
}
Command_room = {

}
Deep_Forest = {
    "name": "Deep Forest",
    "description": "One of the deepest parts of the forest.",
    "structures": outpost,
    "exits": {
        "north": "forest"
    }
}
Dark_Forest = {
    "name": "Dark Forest",
    "description": "The darkest part of the forest.",
    "exits": {
        "north": "Deep_Forest"
    }
}
rooms = {
    "forest": Pine_Forest,
    "cave": cave,
    "inner cave": inner_cave,
    "village": village,
    "The Depths": The_Depths,
    "clearing": clearing,
    "Deep Forest": Deep_Forest,
    "Dark Forest": Dark_Forest,
    "barracks": barracks,
    "outpost entrance": outpost
}

current_room = rooms["forest"]
print("GENERIC ADVENTURE GAME v2.0")

while True:
    print(sword)

    show_stats()
    current_room = rooms["forest"]

    while True:
        if current_room == The_Depths:
            if "torch" in player["inventory"]:
                print("You feel a powerful pressence coming from deeper in the cave. Are you sure you want to do this?")
                print("yes/no")
                choice = input("> ")
                if choice == "yes":
                    print("Don't say I didn't warn you")
                    print(The_Depths["art"])
                elif choice == "no":
                    current_room = inner_cave
            else:
                print("It's too dark to see, you return to the previous layer.")
                current_room = inner_cave
                        
        if player["regen rounds"] > 0:
            player["health"] = min(player["health"] + player["regen"], 100)
            player["regen rounds"] = player["regen rounds"] - 1

        if "enemies" in current_room and len(current_room["enemies"]) > 0:
            print("Enemies appear!")
            while player["health"] > 0 and len(current_room["enemies"]) > 0:
                print(player["health"])
                for i, enemy in enumerate(current_room["enemies"]):
                    print(f"{i + 1}. {enemy['name']} - {enemy['health']} hp")
                print("Do you run, fight, or bandage?")
                action = input("> ")
                if action == "run":
                    if current_room is cave:
                        print("You flee back to the forest.")
                    else:
                        print("You flee all the way back to the forest.")
                    current_room = rooms["forest"]
                    if player["regen rounds"] > 0:
                        player["health"] = min(player["health"] + player["regen"], 100)
                        player["regen rounds"] = player["regen rounds"] - 1
                    break
                elif action == "fight":
                    if any(enemy["name"] == "Necromancer" for enemy in current_room["enemies"]):
                        rng = random.randint(1, 10)
                        if rng in range (1,2):
                            current_room["enemies"].append(copy.deepcopy(skeleton))
                        elif rng in range (2,3):
                            current_room["enemies"].append(copy.deepcopy(zombie))
                    try:
                        target = int(input("Which enemy do you attack?" \
                    " > ")) - 1
                    except ValueError:
                        print("That's not a valid target!")
                        continue
                    current_room["enemies"][target]["health"] = current_room["enemies"][target]["health"] - player["attack"]
                    print(f"The enemy takes {player['attack']} damage")
                    for enemy in current_room["enemies"]:
                        player["health"] = player["health"] - enemy["attack"]
                        print(f"You take {enemy["attack"]} damage from the {enemy['name']}.")
                    if player["regen rounds"] > 0:
                        player["health"] = min(player["health"] + player["regen"], 100)
                        player["regen rounds"] = player["regen rounds"] - 1
                    if current_room["enemies"][target]["health"] <= 0:
                        print(player["health"])
                        print(max(current_room["enemies"][target]["health"], 0))
                        print(f"You have slain the {current_room['enemies'][target]['name']}")
                        player["gold"] = player["gold"] + current_room["enemies"][target]["gold"]
                        current_room["enemies"].pop(target)
                    elif player["health"] <= 0:
                        print("You Died!")
                        player["alive"] = False
                        player["inventory"] = ["sword", "health potion"]
                        player["health"] = 100
                        current_room["enemies"] = current_room["base enemies"]
                        current_room = rooms["forest"]
                        print("You wake up in the forest. You don't know how you got here.")
                        break
                elif action == "bandage":
                    if player["regen rounds"] > 0:
                        player["health"] = min(player["health"] + player["regen"], 100)
                        player["regen rounds"] = player["regen rounds"] - 1
                    if "bandage" in player["inventory"]:
                        player["regen"] = player["regen"] + 5
                        player["regen rounds"] = player["regen rounds"] + 5
                        player["inventory"].remove("bandage")
                    else:
                        print("You don't have a bandage.")
                else:
                    print("You can't do that right now.")

        show_room()

        if "structures" in current_room:
            if current_room["structures"]["name"].startswith(("a", "e", "i", "o", "u", "A", "E", "I","O", "U")):
                print(f"An {current_room['structures']['name']} becomes visible!")
            else:
                print(f"A {current_room['structures']['name']} becomes visible!")
            print("Do you enter? (yes/no)")
            choice = input("> ")
            if choice == "yes":
                current_room = current_room["structures"]
            elif choice == "no":
                show_room()
                pass
            else:
                print("That is not a valid choice")
                continue

        print("inventory to show gear")
        print("drink potion to drink health potion")
        if current_room == village:
            print("shop for merchant")
        print("stats for stats")
        print("quit to leave")
        command = input("> ")

        if command == "quit":
            break
        elif command in current_room["exits"]:
            destination = current_room["exits"][command]
            current_room = rooms[destination]
            if "art" in current_room:
                print(current_room["art"])
        elif command == "inventory":
            for item in player["inventory"]:
                print(item)
            print(f"You have  {player['gold']}  gold.")
        elif command == "drink potion":
            if "health potion" in player["inventory"]: 
                player["health"] = min(player["health"] + 30, 100)
                player["inventory"].remove("health potion")
                print(f"You now have {player['health']} health")
            else:
                print("You don't have a health potion")
        elif command == "shop":
            if current_room == rooms["village"]:
                for key, value in merchant.items():
                    print(f"{value['name']}  -  {value['price']}  gold. {value['description']}")
                print("What do you buy?")
                print(f"You have {player['gold']} gold")
                print("exit to leave shop")
                choice = input("> ")
                if choice in merchant:
                    if player["gold"] >= merchant[choice]["price"]:
                        player["gold"] = player["gold"] - merchant[choice]["price"]
                        player["inventory"].append(merchant[choice]["name"])
                    else:
                        print("You don't have enough gold")
                elif choice == "exit":
                    pass
                else:
                    print("That's not here")
            else:
                print("There's no shop here")
        elif command == "stats":
            show_stats()
        else:
            print("You can't go that way")

    again = input("Keep playing? (y/n) ")
    if again == "n":
        break
