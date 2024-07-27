from bs4 import BeautifulSoup
import requests
import re

def get_raw():
    r = requests.get('https://rotomlabs.net/dex')
    soup = BeautifulSoup(r.content, 'html.parser')
    pokemon = soup.find_all('div', class_ = 'w-auto p-1 text-center mb-2')
    list = []

    for thing in pokemon:
        list.append(thing.get_text())
    
    print(list)
    return list

def format_raw(rlist):
    named_dict = {}

    for mon in rlist:
        sep = mon.split("#")
        sep[1] = sep[1].strip('0123456789')
        types = re.findall('[A-Z][^A-Z]*', sep[1])
        named_dict[sep[0]] = types

    return named_dict

def update_file():
    mydict = format_raw(get_raw())

    with open('pokemon.txt', 'w', encoding="utf-8") as f:
        f.write(str(mydict))

    print("UPDATE SUCCESSFUL")

def update_players(players):
    with open('players.txt','w') as f:
        f.write(str(players))

def update_team(team):
    with open('team.txt','w') as f:
        f.write(str(team))

def format_team(players):
    with open('team.txt', 'w') as f:
        f.write(str(players))

if __name__ == "__main__":
    update_file()
