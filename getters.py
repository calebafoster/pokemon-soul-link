def type_dict():
    mydict = {}

    with open('pokemon.txt', 'r') as f:
        line = f.readline()
        mydict = eval(line)

    return mydict

def player_boxes():
    table = []

    with open('players.txt', 'r') as f:
        line = f.readline()
        table = eval(line)

    return table

def player_team():
    table = []

    with open('team.txt', 'r') as f:
        line = f.readline()
        table = eval(line)

    return table

def players():
    new_table = player_boxes()

    return new_table[0][1:]

def pokemon_type(name):
    return type_dict()[name]
