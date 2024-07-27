import argparse
import update as up
import getters as get
import modes as mode
from tabulate import tabulate
from team import Team

parser = argparse.ArgumentParser(prog='PokemonSoulLinkThing',
                                 description='TODO',
                                 epilog='The End')
parser.add_argument('-u', '--update', action = 'store_true')
parser.add_argument('-ng', '--new_game', type = str,
                    help = "format: Name,Name,Name")
parser.add_argument('-pl','--pokemon_lookup', type = str)
parser.add_argument('-rm', '--remove', action = 'store_true')
parser.add_argument('-a', '--add', action = 'store_true')
parser.add_argument('-t', '--team_builder', action = 'store_true')
args = parser.parse_args()

if args.update:
    up.update_file()

if args.new_game:
    table = []
    table.append(args.new_game.split(','))
    table[0][:0] = ["Name"]
    up.update_players(table)
    up.format_team(get.player_boxes())

if __name__ == "__main__":

    pokemon_dict = get.type_dict()
    player_table = get.player_boxes()
    team_table = get.player_team()

    print('BOX')
    print(tabulate(player_table, headers = 'firstrow'))

    if args.pokemon_lookup:
        print(get.pokemon_type(args.pokemon_lookup))

    if args.add:
        player_table = mode.add(player_table)
        up.update_players(player_table)
        print(tabulate(player_table, headers = 'firstrow'))

    if args.remove:
        player_table = mode.remove(player_table)
        up.update_players(player_table)
        print(tabulate(player_table, headers = 'firstrow'))

    if args.team_builder:
        team = Team(pokemon_dict, player_table, team_table)
        team.menu()
        team.eligible_mons()

    player_table = get.player_boxes()
